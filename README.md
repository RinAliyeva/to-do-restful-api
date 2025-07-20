# RESTful API Task List

ToDo REST API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **JWT Authentication**, and **Docker**.


## Features

- User registration & secure password hashing
- JWT-based user authentication
- CRUD operations for tasks
- Only authorized users can access the API
- Admin user can view all tasks
- Containerized with Docker

## Installation

**1. Clone the repository**
```
git clone https://github.com/RinAliyeva/to-do-restful-api.git
cd to-do-restful-api
```


**2. Start the Services (Docker)**
```
docker-compose up --build

```


API will be running at ``` http://127.0.0.1:8000 ```


**3. Open API docs**
**http://127.0.0.1:8000/docs**

## Usage

To-Do List App is deployed and accessible using Swagger UI.

Create **admin** user to have access to all features.
<img width="1417" height="591" alt="create_admin" src="https://github.com/user-attachments/assets/53164cf7-268e-48aa-9904-dd8b90a016b7" />

After authorization feel free to **create**, **read**, **update**, **delete**, and mark tasks **as completed**.
<img width="1413" height="596" alt="crud" src="https://github.com/user-attachments/assets/3dbedf66-7726-4938-8b70-34e2c455d83a" />

<img width="1413" height="700" alt="upd" src="https://github.com/user-attachments/assets/662a0151-4d64-4cc1-aa4e-4a44def10ff8" />

