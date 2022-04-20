from flask import Flask, render_template, url_for
import books
import customers
import loans

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def index():
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)