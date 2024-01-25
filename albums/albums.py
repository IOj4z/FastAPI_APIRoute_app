from fastapi import APIRouter
from fastapi import FastAPI
from .models import Album

# albums = APIRouter(prefix="/albums", tags=["albums"])
albums = FastAPI()


@albums.get("/albums")
async def get_albums():
    return {"message": "albums"}


@albums.get("/albums/{id}")
async def get_album(id: int):
    return {"message": "album"}


@albums.post("/albums")
async def create_album(a1: Album):
    return {"message": "add album"}


@albums.put("/albums/{id}")
async def update_album(id: int):
    return {"message": "update album"}


@albums.delete("/albums/{id}")
async def delete_album(id: int):
    return {"message": "delete album"}
