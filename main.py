import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {'message': 'Hello from random number api!'}


@app.route('/<int:start>/<int:end>')
def range_(start: int, end: int):
    return {'message': random.randint(start, end)}


if __name__ == '__main__':
    app.run()
