from typing import List

from fastapi import APIRouter, Depends, FastAPI, Header, Request, HTTPException
from typing import Optional
from sqlalchemy import create_engine

from .models import Book
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///mydata.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# books = APIRouter(prefix="/books", tags=["books"])

books = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def verify_header(X_Web_Framework: str = Header()):
    if X_Web_Framework != "FastAPI":
        raise HTTPException(status_code=400, detail="Invalid Header")


@books.middleware("http")
async def add_header(request: Request, call_next):
    print("Message by Middleware before operation function")
    response = await call_next(request)
    response.headers["X-Framework"] = "FastAPI"
    return response


@books.get("/")
async def index(X_Framework: Optional[str] = Header(None)):
    return {"message": "Hello World"}


@books.get("/books", dependencies=[Depends(verify_header)])
async def get_books(db: Session = Depends(get_db)):
    recs = db.query(Book).all()
    return recs


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
