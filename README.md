# Simple Todo API

A simple FastAPI backend to manage todos with CRUD functionality. This API uses a PostgreSQL database running in a Docker container, and migrations are managed with Alembic.

## Requirements

Docker (for PostgreSQL)
Python 3.8+ (for the backend)
Virtual environment (recommended)

## Setup Instructions

1. Clone the Repository

```bash
   git clone https://github.com/your-username/todo-api.git
   cd todo-api
```

2. Set up the Virtual Environment
   Create and activate a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\Activate.ps1
```

3. Install Dependencies

```bash
pip install -r requirements.txt 4. Set Up the Database
```

4. Set Up the Database
   Option A: Using Docker (Recommended)
   Run PostgreSQL in a Docker container:

```bash
docker-compose up -d
```

This will start a PostgreSQL container with the database configured as specified in .env.

Option B: Manually Connect to PostgreSQL
If you're not using Docker, make sure to set the DATABASE_URL in the .env file with your PostgreSQL connection string.

5. Run Alembic Migrations
   Run the Alembic migrations to set up the database schema:

```bash
alembic upgrade head 6. Start the FastAPI App
```

6. Start the FastAPI App
   Start the FastAPI application in development mode:

```bash
fastapi dev
```

The app will now be running at http://localhost:8000.

7. Access the API Documentation
   You can view the interactive API documentation at:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
Environment Variables

8. Testing
   You can run the tests using pytest:

```bash
pytest
```
