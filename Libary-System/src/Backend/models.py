
from sqlalchemy import Column, Integer, String, Boolean, DATE


class Books():
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    isbn = Column(String,index=True)
    title = Column(String,index=True)
    author = Column(String, index=True)
    publisher = Column(String,index=True)
    publishedYear = Column(Integer,index=True)
    isAvailable = Column(Boolean,index=True)

class Loans():
    __tablename__ = "Loans"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    borowedAt = Column(DATE,index=True)
    dueDate = Column(DATE,index=True)
    returnAt = Column(DATE,index=True, nullable=True)
    Status = Column(String,index=True)



