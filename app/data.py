from app.models import Song

# In-memory "database" pre-seeded with 5 songs
songs: list[Song] = [
    Song(
        id=1,
        title="Bohemian Rhapsody",
        artist="Queen",
        genre="Rock",
        release_year=1975,
        album="A Night at the Opera",
    ),
    Song(
        id=2,
        title="Blinding Lights",
        artist="The Weeknd",
        genre="Pop",
        release_year=2019,
        album="After Hours",
    ),
    Song(
        id=3,
        title="Lose Yourself",
        artist="Eminem",
        genre="Hip Hop",
        release_year=2002,
        album="8 Mile Soundtrack",
    ),
    Song(
        id=4,
        title="Imagine",
        artist="John Lennon",
        genre="Pop",
        release_year=1971,
        album="Imagine",
    ),
    Song(
        id=5,
        title="Billie Jean",
        artist="Michael Jackson",
        genre="Pop",
        release_year=1982,
        album="Thriller",
    ),
]
