from datetime import timedelta
import mydatabase
from books import Books
from loans import Loans

#database connection
mydb = mydatabase.MyDB()

# brings all data from a table or specific data from the query(name of a book/customer)
def getdata(table, query = ''): # to get late returns query is used as a simple check but stays unused
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

# adds an object to his table
def addrow(row):
    with mydb.session as session:
        session.add(row)
        session.commit()