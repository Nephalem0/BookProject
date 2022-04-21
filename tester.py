import unittest
import books
import customers
import loans
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///books.db", echo=True, future=True)

Base = declarative_base()

class TestQuery(unittest.TestCase):
    def setUp1(self):
        self.engine = create_engine('sqlite:///books.db')
        self.session = Session(engine)
        Base.metadata.create_all(self.engine)
        self.books = books.Books(1, "adam", "jamie", 1955, 1)
        self.session.add(self.books)
        self.session.commit()

    def tearDown1(self):
        Base.metadata.drop_all(self.engine)

    def test_query_books(self):
        expected = [self.books]
        result = self.session.query(books.Books).all()
        self.assertEqual(result, expected)

    def setUp2(self):
        self.engine = create_engine('sqlite:///books.db')
        self.session = Session(engine)
        Base.metadata.create_all(self.engine)
        self.customers = customers.Customers(1, "joey", "london", 15)
        self.session.add(self.customers)
        self.session.commit()

    def tearDown2(self):
        Base.metadata.drop_all(self.engine)

    def test_query_customers(self):
        expected = [self.customers]
        result = self.session.query(customers.Customers).all()
        self.assertEqual(result, expected)

    def setUp3(self):
        self.engine = create_engine('sqlite:///books.db')
        self.session = Session(engine)
        Base.metadata.create_all(self.engine)
        self.loans = loans.Loans(1, 1)
        self.session.add(self.loans)
        self.session.commit()

    def tearDown3(self):
        Base.metadata.drop_all(self.engine)

    def test_query_loans(self):
        expected = [self.loans]
        result = self.session.query(loans.Loans).all()
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.TestCase()