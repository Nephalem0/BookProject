from sqlalchemy import create_engine
from customers import Customers
from books import Books
from loans import Loans
import db


class MyDB():
    engine = create_engine('sqlite:///books.db', connect_args={'check_same_thread': False}, echo = True)
    db.bind_engine(engine)
    db.Base.metadata.create_all(bind=engine)
    session = db.Session()
