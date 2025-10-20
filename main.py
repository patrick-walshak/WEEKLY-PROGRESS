from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    category: str
    year: int

books = []

@app.post("/post/")
def creat_book(book: Book):
    books.append(book)
    return {"Message": "Book created successfully"}

@app.get("/books/")
def retrieve_book():
    return books

@app.put("/books/{index}")
def update_book(index: int, book: Book):
    books[index] = book
    return {"Message": "Book updated successfully!"}
