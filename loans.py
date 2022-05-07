from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime, timedelta
from books import Books
from customers import Customers
engine = create_engine("sqlite:///books.db", echo=True, future=True)

Base = declarative_base()

class Loans(Base):
    __tablename__ = "loans"
    bookID = Books.id
    customerID = Customers.id
    custID = Column(Integer, ForeignKey(bookID),
                    primary_key=True, nullable=False)
    bookID = Column(Integer, ForeignKey(customerID),
                    primary_key=True, nullable=False)
    loandtate = Column(DateTime, onupdate=datetime.now, nullable=False)
    returndate = Column(DateTime, nullable=False)
