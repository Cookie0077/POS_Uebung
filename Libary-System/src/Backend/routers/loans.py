from click import DateTime
from fastapi import APIRouter
from fastapi_utils.cbv import cbv
import json
from pydantic import BaseModel

from routers.Books import BookCreate

def getjsonData():
    with open("src/Backend/04-01_library_testdata_v2.json", "r") as f:
        data = json.load(f)
    return data

class loanRespone(BaseModel):
    id: int
    bookId: int
    userId: int
    borrowerAT: DateTime
    dueDate: DateTime
    returnAt: DateTime
    status: str


router = APIRouter(prefix="/loans", tags=["loans"])

@cbv(router)
class LoanAPI:

    @router.post("/", response_model=loanRespone)
    def create_loan(self, item:loanRespone):
        data = getjsonData()
        Loan = loanRespone(id=data["loans"][-1]["id"] + 1,bookId=item.bookId, userId=item.userId,
                           borrowerAT=item.borrowerAT, dueDate=item.dueDate,returnAt=item.returnAt,status=item.status)
        data["books"].append(Loan.model_dump())

        with open("04-01_library_testdata_v2.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return Loan
