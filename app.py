from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from books import Books
from customers import Customers
from loans import Loans
import loader

app = Flask(__name__)

engine = create_engine("sqlite:///books.db", echo=True, future=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/book', methods=['GET', 'POST'], defaults={'action': ''})
@app.route('/book/<string:action>', methods=['GET', 'POST'])
def showbook(action):
    if request.method == 'POST':
        return render_template('book.html', action=action, books=loader.getdata(Books, request.form.get('name')))
    elif request.method == 'GET':
        loader.removeitem(Books, request.args.get('id'))
    return render_template('book.html', action=action, God=loader.getdata(Books))


@app.route('/customer', methods=['GET', 'POST'])
@app.route('/customer/<string:action>', methods=['GET', 'POST'])
def showcustomer(action):
    if request.method == 'POST':
        return render_template('customer.html', action=action, customers=loader.getdata(Customers, request.form.get('name')))
    elif request.method == 'GET':
        loader.removeitem(Customers, request.args.get('id'))
    return render_template('customer.html', action=action, customer=loader.getdata(Customers))


@app.route('/addbook', methods=['POST', 'GET'])
def addAbook():
    if request.method == 'POST':
        newbook = Books(id=request.form.get('id'), name=request.form.get('name'), author=request.form.get('author'),
                        year_published=request.form.get('year_published'), type=request.form.get('type'))
        loader.additem(newbook)
        return redirect('/')
    else:
        return render_template('addbook.html')


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
