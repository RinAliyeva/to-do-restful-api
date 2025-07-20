def test_mark_task_completed(client, test_user_with_tasks):
    token = test_user_with_tasks["token"]
    
    tasks_res = client.get(
        "/api/tasks/",
        headers={"Authorization": f"Bearer {token}"}
    )
    task_id = tasks_res.json()[0]["id"]  
    
    
    complete_res = client.post(
        f"/api/tasks/{task_id}/complete",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert complete_res.status_code == 200
    assert complete_res.json()["status"] == "Completed"
    
    
    updated_task = client.get(
        f"/api/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    ).json()
    assert updated_task["status"] == "Completed"

def test_filter_tasks_by_status(client, test_user_with_tasks):
    token = test_user_with_tasks["token"]
    
    
    for status in ["New", "In Progress", "Completed"]:
        filtered_res = client.get(
            f"/api/tasks/status/{status}",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert filtered_res.status_code == 200
        
        tasks = filtered_res.json()
        assert len(tasks) >= 1  
        assert all(task["status"] == status for task in tasks)

def test_filter_invalid_status(client, test_user_with_tasks):
    token = test_user_with_tasks["token"]
    
    
    response = client.get(
        "/api/tasks/status/InvalidStatus",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 422
    assert "detail" in response.json()