"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Model for handling cupcake info."""

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    flavor = db.Column(
        db.Text,
        nullable=False)

    size = db.Column(
        db.Text,
        nullable=False)

    rating = db.Column(
        db.Integer,
        nullable=False)

    image = db.Column(
        db.Text,
        nullable=False,
        default='https://tinyurl.com/demo-cupcake')






