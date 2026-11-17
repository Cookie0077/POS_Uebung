from fastapi import APIRouter
from fastapi_utils.cbv import cbv
import json
from pydantic import BaseModel


def getjsonData():
    with open("src/Backend/04-01_library_testdata_v2.json", "r") as f:
        data = json.load(f)
    return data


class BookCreate(BaseModel):
    title: str
    isbn: str
    author: str
    publisher: str
    publishedYear: int
    isAvailable: bool

class BookResponse(BookCreate):
    id: int


router = APIRouter(prefix="/books", tags=["books"])

@cbv(router)
class BookAPI:
    @router.get("/", response_model=list[BookCreate])
    def get_books(self):
        data = getjsonData()
        return data["books"]

    @router.get("/{id}", response_model=BookCreate)
    def get_book(self, id: int):
        data = getjsonData()
        return data["books"][id]

    @router.post("/", response_model=BookResponse)
    def create_book(self, item:BookResponse):
        data = getjsonData()
        Book = BookResponse(id=data["books"][-1]["id"]+1,title=item.title, isbn=item.isbn, author=item.author,
                          publisher=item.publisher,publishedYear=item.publishedYear, isAvailable=item.isAvailable)
        data["books"].append(Book.model_dump())

        with open("04-01_library_testdata_v2.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return Book

    @router.delete("/{id}", response_model=BookResponse)
    def delete_book(self, id: int):
         data = getjsonData()
         data["books"].pop(id)
         with open("04-01_library_testdata_v2.json", "w", encoding="utf-8") as f:
             json.dump(data, f, indent=4, ensure_ascii=False)

         return {"message": f"Book deleted with {id}"}



