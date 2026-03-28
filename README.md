# Task Manager API

A REST API built with FastAPI and Python.

## Features
- [x] CRUD operations for tasks
- [ ] PostgreSQL database
- [ ] JWT authentication
- [ ] Docker

## Tech Stack
- FastAPI
- Python 3.11

## Run locally
```bash
# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn

# Start server
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /tasks | Get all tasks |
| POST | /tasks | Create a task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

http://127.0.0.1:8000/docs