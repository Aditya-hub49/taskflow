# TaskFlow

TaskFlow is a simple task management API built with FastAPI, SQLAlchemy, and PostgreSQL. It provides user registration, login with JWT authentication, and basic task creation and retrieval.

## Project Overview

This repository implements a lightweight backend service for managing tasks and users. The main responsibilities are:

- User signup and login
- Password hashing and JWT token generation
- Task creation and retrieval
- PostgreSQL database persistence
- Docker-based deployment setup

## Architecture and Project Flow

### Core components

- `app/main.py`
  - Creates the FastAPI application
  - Loads API routers
  - Creates database tables on startup

- `app/api/auth_routes.py`
  - `/signup` endpoint for user registration
  - `/login` endpoint for user authentication

- `app/api/task_routes.py`
  - `/tasks` POST endpoint to create new tasks
  - `/tasks` GET endpoint to list tasks

- `app/core/security.py`
  - Password hashing using `bcrypt`
  - JWT access token creation
  - Password verification

- `app/db/database.py`
  - Database connection setup using SQLAlchemy
  - Provides `get_db()` dependency for request-scoped sessions

- `app/models/user_model.py`
  - SQLAlchemy model for users

- `app/models/task_model.py`
  - SQLAlchemy model for tasks

- `app/schemas/auth_schema.py`
  - Pydantic request models for signup and login

- `app/schemas/task_schema.py`
  - Pydantic schemas for task creation and response

### Request flow

1. Client sends a request to `app/main.py`
2. FastAPI routes the request to the appropriate router:
   - `auth_routes` for authentication requests
   - `task_routes` for task management requests
3. Each route uses `get_db()` to obtain a SQLAlchemy session
4. Business logic executes against the database models
5. The response is returned as JSON

### Authentication flow

1. User submits email and password to `/signup`
2. Server hashes the password and saves the user record
3. User submits email and password to `/login`
4. Server verifies the password and returns a JWT token
5. Token may be used by clients for protected endpoints (future extension)

## API Endpoints

### Health check

- `GET /`
  - Returns a simple JSON response confirming the API is running.

### Authentication

- `POST /signup`
  - Request body: `{ "email": "user@example.com", "password": "secret" }`
  - Registers a new user
  - Returns: `{ "message": "User created successfully" }`

- `POST /login`
  - Request body: `{ "email": "user@example.com", "password": "secret" }`
  - Validates credentials and returns a JWT token
  - Returns: `{ "access_token": "<token>" }`

### Tasks

- `POST /tasks`
  - Request body: `{ "title": "Task title", "description": "Task details" }`
  - Creates a new task
  - Returns the created task object

- `GET /tasks`
  - Retrieves a list of all tasks
  - Returns an array of task objects

## Database Models

### User

- `id`: integer primary key
- `email`: unique email address
- `hashed_password`: bcrypt hashed password

### Task

- `id`: integer primary key
- `title`: task title
- `description`: task description


## Local Setup

1. Create a Python virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create the `.env` file with your `DATABASE_URL`.
4. Run the application:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
5. Open `http://127.0.0.1:8000` to verify the API is running.

## Docker Setup

This repository includes a `docker-compose.yml` with:

- `backend` service for the FastAPI app
- `postgres` service for the PostgreSQL database

To run the application in the background (detached mode):

```bash
docker compose up --build -d
```

Then access the web interface and API at: `http://127.0.0.1:8000`

### Useful Docker Commands

- **Check backend logs (if something goes wrong):**
  ```bash
  docker logs taskflow_backend
  ```
- **Stop the application:**
  ```bash
  docker compose down
  ```
- **Completely reset the database (WARNING: Deletes all user data and tasks):**
  ```bash
  docker compose down -v
  ```

## Future Improvements

- Add task update and delete endpoints.
- Add user profile management.
- Add automated database migrations using Alembic.
