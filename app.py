from flask import Flask, render_template, request, url_for, redirect
import books
import customers
import loans

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/addbook', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        book_id = int(request.form['id'])
        book_name = str(request.form['name'])
        book_author = str(request.form['author'])
        book_year_published = int(request.form['year_published'])
        book_type = int(request.form['type'])
        
        try:
            books.AddBook(book_id,book_name,book_author, book_year_published, book_type)
            return redirect('/')

        except:
            allbooks = books.Books.order_by
            return 'There was an issue adding your book'


    else:
        return render_template('addbook.html')


if __name__ == "__main__":
    app.run(debug=True)
