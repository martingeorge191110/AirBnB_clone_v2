#!/usr/bin/python3
"""script that starts Flask application"""

from flask import Flask, request

server = Flask(__name__)


@server.route("/", strict_slashes=False)
def hello_hbnb():
    """displays Hello HBNB! in / route"""
    return ("Hello HBNB!")


@server.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB in /hbnb route """
    return ("HBNB")


@server.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text variable"""
    textFormated = text.replace('_', ' ')
    return (f"C {textFormated}")


@server.route("/python", strict_slashes=False)
@server.route("/python/<text>", strict_slashes=False)
def python_text(text = 'is cool'):
    """display “Python ” followed by the value of the text variable"""
    return (f"Python {text.replace('_', ' ')}")



if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
