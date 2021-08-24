from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import database_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/graphql')
def empty_for_now():
    return "Graphql endpoint will go here"

