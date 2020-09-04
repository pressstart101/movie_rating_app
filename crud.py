"""CRUD operations"""
from model import db, User, Movie, Rating, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

# UP to: Part 2: "Test that create_user works by running crud.py interactively"