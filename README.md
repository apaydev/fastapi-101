# FastAPI 101

A small workshop where you will learn how to build a simple song/playlist management API using **FastAPI**. You'll implement 6 endpoints that let you create, read, update and delete songs stored in memory (no external DBMS to keep things simple).

## Key Concepts You'll Learn

- Building routes with FastAPI
- Using Pydantic models for request and response validation
- Returning appropriate HTTP status codes
- Handling path parameters and query parameters
- Working with in-memory data and simple CRUD operations

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

Open `app/routes.py` - you'll find 6 endpoint functions that currently just have `pass`. Your job is to implement each one following the instructions in the comments.

> **Tip:** Check out `CHEATSHEET.md` for quick examples of patterns you'll need (raising errors, filtering lists, creating objects, etc.).

### TODO 1: `GET /songs`

Return all songs. If the `genre` query parameter is provided, filter the results (case-insesitive).

**Test it:** Go to `/docs` and try the endpoint with and without the genre filter.

### TODO 2: `GET /songs/stats`

Return statistics about the songs in memory, including the total number of songs, the earliest release year, and a breakdown of songs by genre.

**Test it:** Go to `/docs` and call the endpoint to inspect the returned stats.

### TODO 3: `GET /songs/{song_id}`

Return a single song by its ID. If the song does not exist, return a 404 error with a helpful message.

**Test it:** Try fetching an existing song ID and then a non-existing one.

### TODO 4: `POST /songs`

Create a new song, automatically assign the next ID, add it to the in-memory list, and return the newly created song.

**Test it:** Use `/docs` to send a request with song details and verify that the new song appears in the list.

### TODO 5: `PUT /songs/{song_id}`

Update an existing song by its ID. If the song does not exist, return a 404 error.

**Test it:** Update a song with a valid ID and then try updating one that does not exist.

### TODO 6: `DELETE /songs/{song_id}`

Delete an existing song by its ID. If the song does not exist, return a 404 error. If it exists, return a success message confirming the deletion.

**Test it:** Delete a song from `/docs` and then try deleting it again.

## Useful References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Stuck?

Check `solutions/routes.py` for the complete implementation, but try on your own first!
