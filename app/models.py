from pydantic import BaseModel, Field


class SongCreate(BaseModel):
    """Schema used when creating or updating a song (no id field)."""

    title: str = Field(
        ..., example="Bohemian Rhapsody", description="The title of the song"
    )
    artist: str = Field(..., example="Queen", description="The artist of the song")
    genre: str = Field(..., example="Rock", description="The genre of the song")
    release_year: int = Field(
        ..., example=1975, description="The release year of the song"
    )
    album: str = Field(
        ..., example="A Night at the Opera", description="The album of the song"
    )


class Song(SongCreate):
    """Dull song model including the auto-generated ID field."""

    id: int
