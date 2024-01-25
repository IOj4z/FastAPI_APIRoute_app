import uvicorn
from fastapi import FastAPI
from albums import albums
from books import books

app = FastAPI()


# app.include_router(books.books)
# app.include_router(albums.albums)


@app.get("/stories")
async def root():
    return {"message": "Home page"}


app.mount("/albumapi", albums.albums)
app.mount("/bookapi", books.books)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8881, reload=True)
