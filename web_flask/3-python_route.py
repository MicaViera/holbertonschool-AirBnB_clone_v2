#!/usr/bin/python3
"""Script that starts a Flask web application with four routes."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Method that says hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def holberton_home():
    """Method that says HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Method that says c and text"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Method that replaces and prints."""
    text_replaced = text.replace('_', ' ')
    return "Python " + text_replaced


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
