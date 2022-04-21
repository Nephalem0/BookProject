from flask import Flask, render_template, url_for
import books
import customers
import loans

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/addbook', methods=['POST', 'GET'])
def add():
    return render_template('addbook.html')


if __name__ == "__main__":
    app.run(debug=True)