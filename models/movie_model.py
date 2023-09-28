from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    original_language = db.Column(db.String(50))
    summary = db.Column(db.String(500))
    release_date = db.Column(db.String(10))
    poster_url = db.Column(db.String(255))
    genre = db.Column(db.String(100))
    vote_average = db.Column(db.Float)

    def __init__(self, title, original_language, summary, release_date, poster_url, genre, vote_average):
        self.title = title
        self.original_language = original_language
        self.summary = summary
        self.release_date = release_date
        self.poster_url = poster_url
        self.genre = genre
        self.vote_average = vote_average
