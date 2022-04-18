from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
engine = create_engine("sqlite:///books.db", echo=True, future=True)

Base = declarative_base()

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(30), nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    type = Column(Integer(), nullable=False)

    def __repr__(self):
        return f"books(id={self.id!r}, name={self.name!r}, author={self.author!r}, year_published={self.year_published!r}, type={self.type!r})"

class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    age = Column(String, nullable=False)
    def __repr__(self):
        return f"customers(id={self.id!r}, name={self.name!r}, city={self.city!r}, age={self.age!r})"

class Loans(Base):
    __tablename__ = "loans"
    def BookSelect(type):
        if type == 1:
            return datetime.now() + timedelta(days=10) 
        elif type == 2:
            return datetime.now() + timedelta(days=5)
        elif type == 3:
            return datetime.now() + timedelta(days=2)

    custID = Column(Integer, ForeignKey("Books.id"), nullable=False)
    bookID = Column(Integer, ForeignKey("Customers.id"), nullable=False)
    loandtate = Column(DateTime, onupdate=datetime.now, nullable=False)
    returndate = Column(BookSelect(Integer))
    def __repr__(self):
        return f"loans(id={self.custID!r}, name={self.bookID!r}, city={self.loandtate!r}, age={self.returndate!r})"

Base.metadata.create_all(engine)

def AddBook(id, name, author, year_published, type):
    with Session(engine) as session:
        newbook = Books(
            id = id,
            name = name,
            author = author,
            year_published = year_published,
            type = type
        )
        session.add_all([newbook])
        session.commit()

def AddCustomer(id, name, city, age):
    with Session(engine) as session:
        newcustomer = Customers(
            id = id,
            name = name,
            city = city,
            age = age,
        )
        session.add_all([newcustomer])
        session.commit()

def AddLoan(custID, bookID):
    with Session(engine) as session:
        newloan = Loans(
            custID = custID,
            bookID = bookID
        )
        session.add_all([newloan])
        session.commit()