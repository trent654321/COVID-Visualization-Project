from flask import Flask
from index import hello

app = Flask(__name__)

@app.route('/')
def callIndex():
    return (hello())