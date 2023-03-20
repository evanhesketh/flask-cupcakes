"""Flask app for Cupcakes"""

import os

from flask import Flask, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Cupcake, db

# from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")

connect_db(app)

@app.get('/api/cupcakes')
def get_all_cupcakes_data():
    """
    returns JSON object of cupcakes:

    {cupcakes: [{id, flavor, size, rating, image}, ...]}

    """

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<int:id>')
def get_cupcake_data(id):
    """
    Return JSON about a single cupcake:

    {cupcake: {id, flavor, size, rating, image}}

    """

    cupcake = Cupcake.query.get_or_404(id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post('/api/cupcakes')
def create_cupcake():
    """
    Handle create cupcake request. Save to database.

    Return JSON:
    {cupcake: {id, flavor, size, rating, image}}

    """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image')

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)
