from fastapi import FastAPI, HTTPException
from app.library import Library
from app.external_api import fetch_book_from_api

app = FastAPI(title="Mini Library API")

library = Library()


@app.post("/books")
def add_book(title: str):
    try:
        library.add_book(title)
        return {"status": "ok", "title": title}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/books")
def remove_book(title: str):
    try:
        library.remove_book(title)
        return {"status": "ok", "title": title}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/books")
def list_books():
    return {"books": library.list_books()}


@app.get("/books/search")
def search_books(query: str):
    return {"result": library.search(query)}

@app.get("/external/{book_id}")
def get_book_from_external(book_id: int):
    title = fetch_book_from_api(book_id)
    return {"title": title}