from typing import Any
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository
from datetime import datetime


class MovieRepositoryFixture(MovieRepository):
    def __init__(self) -> None:
        self.movies = [Movie(
            i,
            f"title {i}",
            f"lang {i}",
            f"summary {i}",
            datetime(2000, 2, i),
            f"poster {i}",
            [f"genre {i}", ],
            float(i)
        ) for i in range(1, 9)]

    def list_movies(
        self,
        _page: int,
        filter_tags: list[str] | None = None,
        min_rating: float = 0.0
    ) -> dict[str, Any]:
        movies = [
            movie for movie in self.movies
            if float(movie.vote_average) > min_rating and str(movie.genre)
            and (filter_tags is None or str(movie.genre) in filter_tags)
        ]
        return {
            "movies": movies,
            "total_pages": 1
        }

    def get_movie(self, movie_id: int) -> Movie | None:
        for movie in self.movies:
            if movie.id == movie_id:
                return movie
        return None

    def add_movie(self, movie: Movie) -> Movie:
        return movie
