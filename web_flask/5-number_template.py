#!/usr/bin/python3
"""Script that starts a Flask web application with six routes."""
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


@app.route('/number/<int:n>', strict_slashes=False)
def n_int(n):
    """Displays n is a number only if n is an integer."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display n template if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
