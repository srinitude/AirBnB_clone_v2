#!/usr/bin/python3
"""
Return list of available states either from file or DB storage
"""
from models import storage
from flask import Flask, render_template
from models.state import State
import models


class StateInfo:
    """
    Interface that template receives regardless of storage type
    """
    def __init__(self, id, name):
        """
        State ID and name
        """
        self.id = id
        self.name = name


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """
    Close file/DB storage on app teardown
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    """
    Displays all states
    """
    states = []
    if models.storage_type == "db":
        results = storage.all("State").values()
    else:
        results = storage.all(State).values()
    for result in results:
        new_state = StateInfo(result.id, result.name)
        states.append(new_state)
    states.sort(key=lambda s: s.name)
    return render_template("7-states_list.html",
                           states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
