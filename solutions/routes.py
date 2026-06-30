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
    if genre is None:
        return songs
    return [song for song in songs if song.genre.lower() == genre.lower()]


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
    genre_counts: dict[str, int] = {}
    for song in songs:
        genre_counts[song.genre] = genre_counts.get(song.genre, 0) + 1

    return {
        "total_songs": len(songs),
        "earliest_release_year": min(song.release_year for song in songs),
        "genres": genre_counts,
    }


# ------------------------------------------------------------------------------------
# TODO 3: GET /songs/{song_id}
# Return a single song by its ID. If the song is not found, raise a
# HTTPException with a 404 status code and a message indicating that the song was not found.
# ------------------------------------------------------------------------------------
@router.get("/{song_id}", response_model=Song)
def get_song(song_id: int):
    for song in songs:
        if song.id == song_id:
            return song
    raise HTTPException(status_code=404, detail=f"Song with id {song_id} not found")


# ------------------------------------------------------------------------------------
# TODO 4: POST /songs
# Create a new song. Auto-assign an id (max existing id + 1).
# Append it to the songs list and return the newly created song.
# Hint: Use Song(**song_data.model_dump(), id=new_id). You can also use the max()
# function to find the maximum existing id in the songs list.
# ------------------------------------------------------------------------------------
@router.post("/", response_model=Song, status_code=201)
def create_song(song_data: SongCreate):
    new_id = max((song.id for song in songs), default=0) + 1
    new_song = Song(**song_data.model_dump(), id=new_id)
    songs.append(new_song)
    return new_song


# --------------------------------------------------------------------------------------
# TODO 5: PUT /songs/{song_id}
# Update an existing song by its ID. If the song is not found, raise a
# HTTPException with a 404 status code and a message indicating that the song was not found.
# Hint: Find the index, then update the song in the songs list using that index.
# --------------------------------------------------------------------------------------
@router.put("/{song_id}", response_model=Song)
def update_song(song_id: int, song_data: SongCreate):
    for index, song in enumerate(songs):
        if song.id == song_id:
            updated_song = Song(**song_data.model_dump(), id=song_id)
            songs[index] = updated_song
            return updated_song
    raise HTTPException(status_code=404, detail=f"Song with id {song_id} not found")


# --------------------------------------------------------------------------------------
# TODO 6: DELETE /songs/{song_id}
# Delete an existing song by its ID. If the song is not found, raise a
# HTTPException with a 404 status code and a message indicating that the song was not found.
# If the song is found and deleted, return a message indicating that the song was deleted.
# --------------------------------------------------------------------------------------
@router.delete("/{song_id}")
def delete_song(song_id: int):
    for index, song in enumerate(songs):
        if song.id == song_id:
            del songs[index]
            return {"message": f"Song with id {song_id} deleted"}
    raise HTTPException(status_code=404, detail=f"Song with id {song_id} not found")
