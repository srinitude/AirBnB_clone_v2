#!/usr/bin/python3
"""
Start Flask app with root route
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns a string saying Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns a string saying HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """
    Displays "C", followed by value of <text>
    """
    tokens = text.split("_")
    text = "C " + " ".join(tokens)
    return text


@app.route("/python",
           defaults={'text': "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_text(text):
    """
    Displays "Python", followed by value of <text>
    """
    tokens = text.split("_")
    text = "Python " + " ".join(tokens)
    return text


@app.route("/number/<int:n>", strict_slashes=False)
def print_int(n):
    """
    Prints an integer if number passed is an int
    """
    if type(n) is int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def print_int_template(n):
    """
    Renders special HTML page if number passed is an int
    """
    if type(n) is int:
        return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    Determines if number passed (if int) is odd or even
    """
    if type(n) is int:
        odd = n % 2
        if odd:
            d = "odd"
        else:
            d = "even"
        return render_template("6-number_odd_or_even.html",
                               number=n,
                               divisibility=d)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
