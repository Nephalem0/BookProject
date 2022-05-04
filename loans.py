from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from books import Books
from customers import Customers
engine = create_engine("sqlite:///books.db", echo=True, future=True)

Base = declarative_base()

class Loans(Base):
    __tablename__ = "loans"

    def BookSelect(type):
        if type == 1:
            return datetime.now() + timedelta(days=10)
        elif type == 2:
            return datetime.now() + timedelta(days=5)
        elif type == 3:
            return datetime.now() + timedelta(days=2)
    bookID = Books.id
    customerID = Customers.id
# REMEMBER TO CHECK HOW TO DO THIS WITHOUT A PRIMARY KEY!!!!!!
    custID = Column(Integer, ForeignKey(bookID),
                    primary_key=True, nullable=False)
    bookID = Column(Integer, ForeignKey(customerID),
                    primary_key=True, nullable=False)
    loandtate = Column(DateTime, onupdate=datetime.now, nullable=False)
    returndate = Column(DateTime, BookSelect(Integer))
    # check later

    def __repr__(self):
        return f"loans(id={self.custID!r}, name={self.bookID!r}, city={self.loandtate!r}, age={self.returndate!r})"


Base.metadata.create_all(engine)


def AddLoan(cust_ID, book_ID):
    with Session(engine) as session:
        newloan = Loans(
            custID=cust_ID,
            bookID=book_ID
        )
        session.add_all([newloan])
        session.commit()


def get_table_metadata(engine, table):
    metadata = MetaData()
    metadata.reflect(bind=engine, only=[table])
    table_metadata = Table(table, metadata, autoload=True)
    return table_metadata
