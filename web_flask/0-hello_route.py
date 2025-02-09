#!/usr/bin/python3
"""script that starts Flask application"""

from flask import Flask

server = Flask(__name__)


@server.route("/", strict_slashes=False)
def hello_hbnb():
    """displays Hello HBNB! in / route"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
