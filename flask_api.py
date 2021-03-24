"""
Defines a flask api with a single endpoint for getting an idea string
"""
from flask import Flask
from flask import request
import random
from sentence_components import *

app = Flask(__name__)  # create a flask app object


# key that is required to hit api (prevents random people sniffing ip's from having access)
real_key = "DgGl3ju8ftRF494B7kQAInDl80bWqUbeG6hQBRgCI52MknkLhv61dVlpZflfjhHDC2Y9Nk3wcd7tDQVUK9usW34CZ1r7wCxf18PZ"


@app.route('/randidea')
def rand_idea():
    global real_key
    key = request.args.get('key', default=None) # get the key argument
    if key == real_key:
        seed = request.args.get('seed', default=-1) # get the seed argument if it exists
        idea = ComponentRegistry.get_traversed_sentence(seed)
        return idea
    else:
        return "403 forbidden" # forbidden


if __name__ == '__main__':
    app.run()