from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from books import Books
from customers import Customers
from loans import Loans
import loader


app = Flask(__name__)

engine = create_engine("sqlite:///books.db", echo=True, future=True)

def BookSelect(type):
    if type == 1:
        return datetime.now() + timedelta(days=10)
    elif type == 2:
        return datetime.now() + timedelta(days=5)
    elif type == 3:
        return datetime.now() + timedelta(days=2)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/book', methods=['GET', 'POST'], defaults={'action': ''})
def showbook(action):
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('book.html', action=action, book=loader.getdata(Books, name=name))
    elif request.method == 'GET':
        loader.removeitem(Books, request.args.get('id'))
    return render_template('book.html', action=action, book=loader.getdata(Books))


@app.route('/addbook', methods=['POST', 'GET'])
def addAbook():
    if request.method == 'POST':
        newbook = Books(id=request.form.get('id'), name=request.form.get('name'), author=request.form.get('author'),
                        year_published=request.form.get('year_published'), type=request.form.get('type'))
        loader.additem(newbook)
        return redirect('/')
    else:
        return render_template('addbook.html')


@app.route('/customer', methods=['GET', 'POST'], defaults={'action': ''})
def showcustomer(action):
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('customer.html', action=action, customer=loader.getdata(Customers, name=name))
    elif request.method == 'GET':
        loader.removeitem(Customers, request.args.get('id'))
    return render_template('customer.html', action=action, customer=loader.getdata(Customers))


@app.route('/addcustomer', methods=['POST', 'GET'])
def addAcustomer():
    if request.method == 'POST':
        newcustomer = Customers(id=request.form.get('id'), name=request.form.get('name'), city=request.form.get('city'),
                                age=request.form.get('age'))
        loader.additem(newcustomer)
        return redirect('/')
    else:
        return render_template('addcustomer.html')


if __name__ == "__main__":
    app.run(debug=True)
