from sqlalchemy import create_engine
import db


class MyDB():
    engine = create_engine("sqlite:///books.db", echo=True, future=True)
    db.bind_engine(engine)
    db.Base.metadata.create_all(bind=engine)
    session = db.Session()
