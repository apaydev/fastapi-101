# Cheatsheet

Quick reference for the patterns you'll need to complete the TODOs.

## 1. Raise an HTTP error

Use `HTTPException` when a resource is missing or invalid.

```python
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="Song with id 0000 not found")
```

The `detail` message will be included in the JSON response body.

## 2. Create an object from a Pydantic model

When you receive data from a request body, you can turn it into a model instance and then add extra fields such as an ID.

```python
from app.models import Song, SongCreate

new_id = 6 # Good enough for this workshop, but see the notes at the end of this document for ID generation in production environments.
song = Song(**song_data.model_dump(), id=new_id)
```

`model_dump()` convers the Pydantic model to a dictionary, and `**` unpacks it as keyword arguments.

**What are keyword arguments?** They're arguments passed by name rather than position.

```python
# These two calls are equivalent
Book(title="The Hobbit", author="Tolkien", pages="310", id="1")

data = {"title": "The Hobbit", "author": "Tolkien", "pages": 310}
Book(**data, id=1) # ** unpacks the dict into keyword arguments
```

## 3. Filter a list

You can filter items from a list using a regular `for` loop:

```python
# Example: filter numbers greater than 5
numbers = [1, 8, 3, 10, 2, 7]
results = []
for n in numbers:
  if n > 5:
    results.append(n)
# results = [8, 10, 7]
```

A more compact alternative is a **list comprehension** (same result, one line):

```python
results = [n for n in numbers if n > 5]
```

If no items match, both approaches return an empty list `[]`.

## 4. Find an item by ID

You can loop through the list and return early when you find whay you are looking for. This is also known as a _Guard Clause_:

```python
for book in books:
  if book.id == book_id:
    return book
# If we get to this part of the code, then nothing was found, so we need to raise an exception
raise HTTPException(status_code=404, detail="Not found")
```

## 5. Auto-increment an ID

For this in-memory example, you can compute the next ID from the highest existing one.

```python
new_id = max((item.id for item in items), default=0) + 1
```

- The generator `(item.id for item in items)` extracts all IDs
- `default=0` handles the case where the list is empty
- `+ 1` gives us the next available id

## 6.Return a response with a status code

By default, FastAPI returns `200 OK`. You can define the success status code directly on the route decorator.

```python
# We are using "201 Created", which is a status code that shows to the user that a resource has been created correclty.
@router.post("/", response_model=Song, status_code=201)
def create_song(song_data: SongCreate):
    ...
```

## In Production ...

The patterns above are perfect for learning, but here's what changes in real world applications:
**ID Generation**: `max(...) + 1` works here because we have a single process and no real concurrency. In a production environment:

- **Databases** handle this automatically (`SERIAL` / `AUTOINCREMENT` columns)
- **UUIDs** avoid coordination entirely, which means that there is no need to check existing IDs in order to calculate a new one, or to avoid duplication.

**Data Storage**: Our in-memory list resets every time the server restarts. Real APIs use databases (PostgreSQL, MongoDB, etc.) for persistance.

**Validation**: We keep it simple with sring matching for fiels like `genre`. Production APIs often use `Enum` types to restrict values to a predefined set.

Don't worry too much about these for now - the goal here is to learn FastAPI's core patterns. You'll have plenty of time to worry about these in the future!
