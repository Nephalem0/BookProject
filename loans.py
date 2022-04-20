from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
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
# REMEMBER TO CHECK HOW TO DO THIS WITHOUT A PRIMARY KEY!!!!!!
    custID = Column(Integer, ForeignKey("books.id"),
                    primary_key=True, nullable=False)
    bookID = Column(Integer, ForeignKey("customers.id"),
                    primary_key=True, nullable=False)
    loandtate = Column(DateTime, onupdate=datetime.now, nullable=False)
    returndate = Column(DateTime, BookSelect(Integer))
    # check later

    def __repr__(self):
        return f"loans(id={self.custID!r}, name={self.bookID!r}, city={self.loandtate!r}, age={self.returndate!r})"


Base.metadata.create_all(engine)


def AddLoan(custID, bookID):
    with Session(engine) as session:
        newloan = Loans(
            custID=custID,
            bookID=bookID
        )
        session.add_all([newloan])
        session.commit()