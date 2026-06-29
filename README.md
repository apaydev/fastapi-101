# FastAPI 101

A small workshop where you will learn how to build a simple song/playlist management API using **FastAPI**. You'll implement 6 endpoints that let you create, read, update and delete songs stored in memory (no external DBMS to keep things simple).

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- A code editor (VS Code recommended)
- Git

## Setup

1. **Clone/download this repository on your local machine and move inside of the directory:**

```bash
git clone https://github.com/apaydev/fastapi-101.git && cd fastapi-101/
```

2. **Create a virtual environment inside of the workshop directory:**

```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the server:**

```bash
fastapi dev
```

5. **Open the interactive docs by visiting http://127.0.0.1:8000/docs (Swagger UI) or http://127.0.0.1:8000/redoc (ReDoc)**

## Your Task
