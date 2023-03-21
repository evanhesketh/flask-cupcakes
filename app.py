"""Flask app for Cupcakes"""

import os

from flask import Flask, request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Cupcake, db

# from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")

connect_db(app)

@app.get('/')
def index():
    """Display homepage."""

    return render_template('index.html')

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
    image = request.json['image'] if request.json['image'] else None

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

@app.patch('/api/cupcakes/<int:id>')
def update_cupcake(id):
    """
    Update cupcake

    Return JSON:
    {cupcake: {id, flavor, size, rating, image}}

    """

    cupcake = Cupcake.query.get_or_404(id)
    data = request.json

    cupcake.flavor = data.get('flavor') if data.get('flavor') else cupcake.flavor
    cupcake.size = data.get('size') if data.get('size') else cupcake.size
    cupcake.rating = data.get('rating') if data.get('rating') else cupcake.rating
    cupcake.image = data.get('image') if data.get('image') else cupcake.image

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.delete('/api/cupcakes/<int:id>')
def delete_cupcake(id):
    """
    Delete cupcake

    Return JSON:
    {deleted: [cupcake-id]}

    """
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)

    db.session.commit()

    return jsonify(deleted=[id])


