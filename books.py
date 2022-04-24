from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
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


Base.metadata.create_all(engine)


def AddBook(id, name, author, year_published, type):
    with Session(engine) as session:
        newbook = Books(
            id=id,
            name=name,
            author=author,
            year_published=year_published,
            type=type
        )
        session.add_all([newbook])
        session.commit()


def get_table_metadata(engine, table):
    metadata = MetaData()
    metadata.reflect(bind=engine, only=[table])
    table_metadata = Table(table, metadata, autoload=True)
    return table_metadata
