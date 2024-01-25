import uvicorn
from fastapi import FastAPI, Depends

import persons
from albums import albums
from books import books
from persons import persons

app = FastAPI()

app.mount("/albumapi", albums.albums)
app.mount("/bookapi", books.books)
app.mount("/personapi", persons.persons)




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
