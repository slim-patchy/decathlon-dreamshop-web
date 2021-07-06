from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# Initialise SQLAlchemy to be used in the models
db = SQLAlchemy()

app = Flask(__name__)


@app.route('/')
# def hello_world():
#     return 'Hello World!'
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
