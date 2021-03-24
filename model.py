"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


# Replace this with your code!


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

class User(db.Model):
    """A user table class"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, 
                        unique=True)
    password = db.Column(db.String)

    # ratings = a list of Rating objects
            
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} Also, you look great today.>'

class Movie(db.Model):
    """Movie table class"""

    __tablename__ = 'movies'
    
    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    # ratings = a list of Rating objects

    def __repr__(self):
        return f'<Movies movie_id={self.movie_id} title={self.title}. Your hair looks amazing today.>'


class Rating(db.Model):
    """A rating table class"""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    movie_id = db.Column(db.Integer,
                        db.ForeignKey('movies.movie_id')) 
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))
    score = db.Column(db.Integer)
    
    movie = db.relationship('Movie', backref='ratings') #(backref = 'ratings') is to tie the Movies table to Ratings Table to be able to call to ratings attribute
    user = db.relationship('User', backref='ratings')#(backref = 'ratings') is to tie the Users table to Ratings Table

         
    def __repr__(self):
        return f'<Ratings rating_id={self.rating_id} score= {self.score} Thank you for being a fun person.>'


#bd.create_all() is to create all the tables with the details above in python class


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
