from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
engine = create_engine("sqlite:///books.db", echo=True, future=True)

Base = declarative_base()


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    age = Column(String, nullable=False)

    def __repr__(self):
        return f"customers(id={self.id!r}, name={self.name!r}, city={self.city!r}, age={self.age!r})"


Base.metadata.create_all(engine)


def AddCustomer(id, name, city, age):
    with Session(engine) as session:
        newcustomer = Customers(
            id=id,
            name=name,
            city=city,
            age=age,
        )
        session.add_all([newcustomer])
        session.commit()
