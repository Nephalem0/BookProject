from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import books
import customers
import loans

app = Flask(__name__)

engine = create_engine("sqlite:///books.db", echo=True, future=True)


@app.route('/',  methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/book')
def showbook():
    book = books.get_table_metadata(engine, 'booklist')
    return render_template('book.html').format(book=book)


@app.route('/addbook', methods=['POST', 'GET'])
def addAbook():
    if request.method == 'POST':
        book_id = int(request.form['id'])
        book_name = str(request.form['name'])
        book_author = str(request.form['author'])
        book_year_published = int(request.form['year_published'])
        book_type = int(request.form['type'])

        try:
            books.AddBook(book_id, book_name, book_author,
                          book_year_published, book_type)
            return redirect('/')

        except:
            return 'There was an issue adding your book'

    else:
        return render_template('addbook.html')


@app.route('/addcustomer', methods=['POST', 'GET'])
def addAcustomer():
    if request.method == "POST":
        customer_id = int(request.form['id'])
        customer_name = str(request.form['name'])
        customer_city = str(request.form['city'])
        customer_age = int(request.form['age'])
        try:
            customers.AddCustomer(customer_id, customer_name,
                                  customer_city, customer_age)
            return redirect('/')

        except:
            return 'There was an issue adding your customer'

    else:
        return render_template('addcustomer.html')


@app.route('/addloan', methods=['POST', 'GET'])
def addloan():
    if request.method == "POST":
        customer_ID = int(request.form['custID'])
        book_ID = int(request.form['bookID'])
        try:
            loans.AddLoan(customer_ID, book_ID)
            return redirect('/')

        except:
            return 'There was an issue adding your loan'

    else:
        return render_template('addloan.html')


if __name__ == "__main__":
    app.run(debug=True)
