from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# Initialise SQLAlchemy to be used in the models
db = SQLAlchemy()

app = Flask(__name__)


# Frontend
@app.route('/')
# def hello_world():
#     return 'Hello World!'
def index():
    return render_template('index.html')


@app.route('/cart')
def shopping_cart():
    return render_template('cart.html')


@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
