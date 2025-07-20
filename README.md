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

This project includes unit tests that run automatically upon docker-compose up --build.
API will be running at ``` http://127.0.0.1:8000 ```


**3. Open API docs**
**http://127.0.0.1:8000/docs**

## Usage

To-Do List App is deployed and accessible using Swagger UI.

Create **admin** user to have access to all features.
<img width="1417" height="591" alt="create_admin" src="https://github.com/user-attachments/assets/53164cf7-268e-48aa-9904-dd8b90a016b7" />

After authorization feel free to **create**, **read**, **update**, **delete**, and mark tasks **as completed** and many other functions.
<img width="1413" height="596" alt="crud" src="https://github.com/user-attachments/assets/3dbedf66-7726-4938-8b70-34e2c455d83a" />

<img width="1132" height="789" alt="readtask" src="https://github.com/user-attachments/assets/2af66271-782f-4a02-a2c1-bfa626973710" />

<img width="1413" height="700" alt="upd" src="https://github.com/user-attachments/assets/662a0151-4d64-4cc1-aa4e-4a44def10ff8" />

<img width="1414" height="904" alt="delete" src="https://github.com/user-attachments/assets/fb54a9a4-331f-4303-9598-1c63f82dbc50" />
