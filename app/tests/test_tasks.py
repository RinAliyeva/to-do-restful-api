def test_mark_task_completed(client, test_user_with_tasks):
    token = test_user_with_tasks["token"]
    
    # Get initial tasks
    tasks_res = client.get(
        "/api/tasks/",
        headers={"Authorization": f"Bearer {token}"}
    )
    task_id = tasks_res.json()[0]["id"]  # Get first task ID
    
    # Mark as completed
    complete_res = client.post(
        f"/api/tasks/{task_id}/complete",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert complete_res.status_code == 200
    assert complete_res.json()["status"] == "Completed"
    
    # Verify update
    updated_task = client.get(
        f"/api/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    ).json()
    assert updated_task["status"] == "Completed"

def test_filter_tasks_by_status(client, test_user_with_tasks):
    token = test_user_with_tasks["token"]
    
    # Test each status filter
    for status in ["New", "In Progress", "Completed"]:
        filtered_res = client.get(
            f"/api/tasks/status/{status}",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert filtered_res.status_code == 200
        
        tasks = filtered_res.json()
        assert len(tasks) >= 1  # At least one task per status
        assert all(task["status"] == status for task in tasks)

def test_filter_invalid_status(client, test_user_with_tasks):
    token = test_user_with_tasks["token"]
    
    # Test with invalid status (should return 422)
    response = client.get(
        "/api/tasks/status/InvalidStatus",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 422
    assert "detail" in response.json()