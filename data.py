from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///BookStore.db', echo=True)
session = sessionmaker(bind=engine)()

Base = declarative_base()


class Books(Base):
    __tablename__ = "Books"

    ID = Column('ID', Integer, primary_key=True)
    Name = Column('Name', String)
    Author = Column('Author', String)
    Year_Published = Column('Year_Published', Integer)
    Type = Column('Type', Integer)

    def __init__(self, ID, Name, Author, Year_Published, Type):
        self.ID = ID
        self.Name = Name
        self.Author = Author
        self.Year_Published = Year_Published
        self.Type = Type


class Customers(Base):
    __tablename__ = "Costumers"

    ID = Column('ID', Integer, primary_key=True)
    Name = Column('Name', String)
    City = Column('City', String)
    Age = Column('Age', Integer)

    def __init__(self, ID, Name, City, Age):
        self.ID = ID
        self.Name = Name
        self.City = City
        self.Age = Age


class Loans(Base):
    __tablename__ = "Loans"

    CustID = Column('CustID', Integer, primary_key=True)
    BookID = Column('BookID', Integer)
    Loandate = Column('Loandate', Integer)
    ReturnDate = Column('ReturnDate', Integer)

    def __init__(self, CustID, BookID, Loandate, ReturnDate):
        self.CustID = CustID
        self.BookID = BookID
        self.Loandate = Loandate
        self.ReturnDate = ReturnDate

books = Books(1, "James", "adam", 1515, 1)
session.add(books)
session.commit()
