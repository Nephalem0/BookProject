from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from books import Books
from customers import Customers
from loans import Loans
import loader
 
app = Flask(__name__)

engine = create_engine("sqlite:///books.db", echo=True, future=True)


@app.route('/',  methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/book')
def showbook():
    return render_template('book.html', book = loader.getdata(Books))


@app.route('/addbook', methods=['POST', 'GET'])
def addAbook():
    if request.method == 'POST':
        newbook = Books(id=request.form.get('id'), name=request.form.get('name'), author=request.form.get('author'),
                        year_published=request.form.get('year_published'), type=request.form.get('type'))
        loader.addrow(newbook)
        return redirect('/')
    else:
        return render_template('addbook.html')


if __name__ == "__main__":
    app.run(debug=True)



        #book_id = int(request.form['id'])
        #book_name = str(request.form['name'])
        #book_author = str(request.form['author'])
        #book_year_published = int(request.form['year_published'])
        #book_type = int(request.form['type'])
        # try:
        #    newbook = books.Books(book_id, book_name, book_author,
        #                        book_year_published, book_type)
        #    loader.addrow(newbook)
        #    return redirect('/')

        # except:
        #    return 'There was an issue adding your book'