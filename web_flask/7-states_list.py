#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


server = Flask(__name__)


@server.teardown_appcontext
def close_session(exception):
    storage.close()


@server.route("/states_list", strict_slashes=False)
def list_states():
    """renders all of the states in html file"""
    states = storage.all(State)

    return (render_template("7-states_list.html", states=states.values()))


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
