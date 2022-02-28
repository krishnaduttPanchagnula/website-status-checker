from tester import test
from flask import flask

app = Flask(__name__)

@app.route('/')
def home():
    return test
