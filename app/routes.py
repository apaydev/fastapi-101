from fastapi import APIRouter, HTTPException

from app.data import songs
from app.models import Song, SongCreate

router = APIRouter(prefix="/songs", tags=["songs"])


# ------------------------------------------------------------------------------------
# TODO 1: GET /songs
# Reutn all songs. If the optional query parameter @genre@ is provided,
# filter the list to only include songs matching that gehre (case-insesitive).
# Hint: You can use a list comprehension to filter the songs.
# ------------------------------------------------------------------------------------
@router.get("/", response_model=list[Song])
def get_songs(genre: str | None = None):
    pass


# ------------------------------------------------------------------------------------
# TODO 2: GET /songs/stats
# Return stitstics about the songs in the database, including:
# - total number of songs
# - the earliest release year
# - a dictionary with genre names as keys and the number of songs in each genre as values
# Hint: You can use a loop or collections.Counter to count the number of songs in each genre.
# ------------------------------------------------------------------------------------
@router.get("/stats")
def get_song_stats():
    pass


# ------------------------------------------------------------------------------------
# TODO 3: GET /songs/{song_id}
# Return a single song by its ID. If the song is not found, raise a
# HTTPException with a 404 status code and a message indicating that the song was not found.
# ------------------------------------------------------------------------------------
@router.get("/{song_id}", response_model=Song)
def get_song(song_id: int):
    pass


# ------------------------------------------------------------------------------------
# TODO 4: POST /songs
# Create a new song. Auto-assign an id (max existing id + 1).
# Append it to the songs list and return the newly created song.
# Hint: Use Song(**song_data.model_dump(), id=new_id). You can also use the max()
# function to find the maximum existing id in the songs list.
# ------------------------------------------------------------------------------------
@router.post("/", response_model=Song, status_code=201)
def create_song(song_data: SongCreate):
    pass


# --------------------------------------------------------------------------------------
# TODO 5: PUT /songs/{song_id}
# Update an existing song by its ID. If the song is not found, raise a
# HTTPException with a 404 status code and a message indicating that the song was not found.
# Hint: Find the index, then update the song in the songs list using that index.
# --------------------------------------------------------------------------------------
@router.put("/{song_id}", response_model=Song)
def update_song(song_id: int, song_data: SongCreate):
    pass


# --------------------------------------------------------------------------------------
# TODO 6: DELETE /songs/{song_id}
# Delete an existing song by its ID. If the song is not found, raise a
# HTTPException with a 404 status code and a message indicating that the song was not found.
# If the song is found and deleted, return a message indicating that the song was deleted.
# --------------------------------------------------------------------------------------
@router.delete("/{song_id}")
def delete_song(song_id: int):
    pass
