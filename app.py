import flask
import json


app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])

def home():
    data = json.load(open('task.json'))
    return data

