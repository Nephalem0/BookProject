from datetime import datetime, timedelta
import mydatabase
from books import Books
from loans import Loans

mydb = mydatabase.MyDB()


def getdata(table, name=''):
    if name == '':
        if table == Loans:
            info = mydb.session.query(table).order_by(table.loandate).all()
        else:
            info = mydb.session.query(table).order_by(table.name).all()
    elif table == Loans:
        info = mydb.session.query(table).filter(table.islate).all()
    else:
        info = mydb.session.query(table).filter(table.name.like(f'%{name}%')).all()
    return info


def additem(item):
    with mydb.session as session:
        session.add(item)
        session.commit()


def removeitem(table, rid):
    with mydb.session as session:
        session.query(table).filter(table.id == rid).delete()
        session.commit()


def removeitemloan(table, ridCust, ridBook):
    with mydb.session as session:
        session.query(table).filter(table.bookID == ridBook, table.custID == ridCust).delete()
        session.commit()


def isreturnlate():
    with mydb.session as session:
        for row in session.query(Loans).all():
            if row.returndate > datetime.now():
                row.islate = True
        return session.query(Loans).filter(Loans.islate).all()



def getBookFromId(bookid):
    with mydb.session as session:
        return session.query(Books).get(bookid)
