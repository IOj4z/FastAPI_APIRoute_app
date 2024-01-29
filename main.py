import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware

import persons
from albums import albums
from books import books
from persons import persons

app = FastAPI()

app.mount("/albumapi", albums.albums)
app.mount("/bookapi", books.books)
app.mount("/personapi", persons.persons)
origins = [
    "http://localhost",
    "http://127.0.0.1:8881"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.middleware("http")
async def add_header(request: Request, call_next):
    print("Message by Middleware before operation function")
    response = await call_next(request)
    response.headers["X-Framework"] = "FastAPI"
    return response


# app.include_router(books.books)
# app.include_router(albums.albums)

def dow():
    from datetime import datetime
    dow = datetime.now().weekday()
    return dow


@app.get("/")
async def root(day=Depends(dow)):
    if day == 6:
        return {"message": "Service not available on Sunday"}
    return {"message": "Home page"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8881, reload=True)
