#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


server = Flask(__name__)


@server.teardown_appcontext
def close_session(exception):
    storage.close()


@server.route("/states", strict_slashes=False)
@server.route("/states/<id>", strict_slashes=False)
def list_states(id=None):
    """renders all states in html"""
    states = storage.all(State)
    response_states = []

    if id:
        for state in states.values():
            if id == state.id:
                response_states = state
    else:
        for state in states.values():
            response_states.append(state)

    return (render_template("9-states.html", states=response_states, id=id))


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
