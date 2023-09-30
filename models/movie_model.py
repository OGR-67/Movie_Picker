from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

db: SQLAlchemy = SQLAlchemy()


class Movie(Model):
    __tablename__ = 'movies'

    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(255), nullable=False)
    original_language: str = db.Column(db.String(50))
    summary: str = db.Column(db.String(500))
    release_date: str = db.Column(db.String(10))
    poster_url: str = db.Column(db.String(255))
    genre: str = db.Column(db.String(100))
    vote_average: float = db.Column(db.Float)

    def __init__(self, title: str, original_language: str, summary: str, release_date: str, poster_url: str, genre: str, vote_average: float):
        self.title = title
        self.original_language = original_language
        self.summary = summary
        self.release_date = release_date
        self.poster_url = poster_url
        self.genre = genre
        self.vote_average = vote_average
