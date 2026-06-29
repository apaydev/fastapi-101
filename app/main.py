from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Songs API",
    description="A simple API for managing songs - FastAPI 101 Workshop",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to the Songs API! Visit /docs for API documentation."}
