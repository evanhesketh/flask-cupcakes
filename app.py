"""Flask app for Cupcakes"""

import os

from flask import Flask, render_template, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Cupcake, db

# from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")

connect_db(app)

@app.get('/api/cupcakes')
def get_cupcake_data():
    """returns JSON object of cupcakes

    {cupcakes: [{id, flavor, size, rating, image}, ...]}

    """

    #get all data from database
    cupcakes = Cupcake.query.all()
    #serialize our cupcakes data
    serialized = [cupcake.serialize() for cupcake in cupcakes]
    #return our cupcakes data in json
    return jsonify(cupcakes=serialized)
