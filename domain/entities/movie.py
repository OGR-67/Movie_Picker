from dataclasses import dataclass
from datetime import date


@dataclass
class Movie:
    id: int
    title: str
    original_language: str
    summary: str
    release_date: date
    poster_url: str
    genre: list[str]
    vote_average: float


AVAILABLE_GENRE = [
    "action",
    "adventure",
    "animation",
    "comedy",
    "crime",
    "documentary",
    "drama",
    "family",
    "fantasy",
    "history",
    "horror",
    "music",
    "mystery",
    "romance",
    "science_fiction",
    "tv_movie",
    "thriller",
    "war",
    "western"
]
