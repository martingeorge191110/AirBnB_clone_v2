#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


server = Flask(__name__)


@server.teardown_appcontext
def close_session(exception):
    storage.close()


@server.route("/cities_by_states", strict_slashes=False)
def list_states():
    """renders all states in html"""
    states = storage.all(State)

    return (render_template("8-cities_by_states.html", states=states.values()))


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
