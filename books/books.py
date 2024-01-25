from fastapi import APIRouter
from fastapi import FastAPI
from .models import Book
# books = APIRouter(prefix="/books", tags=["books"])

books = FastAPI()




@books.get("/books")
async def get_books():
    return {"message": "pass"}


@books.get("/books/{id}")
async def get_book(id: int):
    return {"message": "pass"}


@books.post("/books")
async def add_book(b1: Book):
    return {"message": "pass"}


@books.put("/books/{id}")
async def update_book(id: int):
    return {"message": "pass"}


@books.delete("/books/{id}")
async def delete_book(id: int):
    return {"message": "pass"}
