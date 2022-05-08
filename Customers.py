from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import db


class Customers(db.Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
