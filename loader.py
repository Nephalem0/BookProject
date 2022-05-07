from datetime import timedelta
import mydatabase
from books import Books
from loans import Loans


mydb = mydatabase.MyDB()


def getdata(table, query = ''):
    if query == '':
        if table == Loans:
            info = mydb.session.query(table).order_by(table.loan_date).all()
        else:    
            info = mydb.session.query(table).order_by(table.name).all()
    elif table == Loans:
        info = mydb.session.query(table).filter(table.islate == True).all()
    else:
        info = mydb.session.query(table).filter(table.name.like(f'%{query}%')).all()
    return info


def addrow(row):
    with mydb.session as session:
        session.add(row)
        session.commit()


def removerow(table,rid):
    with mydb.session as session:
        session.query(table).filter(table.rowid == rid).delete()
        session.commit()

def returnloan(loanid, date):
    with mydb.session as session:
        session.query(Loans).filter(Loans.loan_id == loanid).update({"return_date": date})
        for loan in session.query(Loans).filter(Loans.loan_id == loanid).all():
            loan.bookname.isloaned = False
        session.commit()

def isreturnlate(loanid):
    with mydb.session as session:
        for l in session.query(Loans).filter(Loans.loan_id == loanid).all():
            if l.bookname.book_type == 1:
                if l.return_date - l.loan_date < timedelta(days = 10):
                    session.query(Loans).filter(Loans.loan_id == loanid).update({"islate": False})
            elif l.bookname.book_type == 2:
                if l.return_date - l.loan_date < timedelta(days = 5):
                    session.query(Loans).filter(Loans.loan_id == loanid).update({"islate": False})
            else:
                if l.return_date - l.loan_date < timedelta(days = 2):
                    session.query(Loans).filter(Loans.loan_id == loanid).update({"islate": False})
        session.commit()

def loanedbook(bookid):
    with mydb.session as session:
        session.query(Books).filter(Books.rowid == bookid).update({"isloaned": True})
        session.commit()

def bookcheck(bookid):
    with mydb.session as session:
        for book in session.query(Books).filter(Books.rowid == bookid):
            if book.isloaned:
                return False
            return True