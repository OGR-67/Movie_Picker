from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository
from unittest.mock import Mock
from datetime import datetime


class MovieRepositoryFixture:
    movies = [Movie(
        i,
        f"title {i}",
        f"lang {i}",
        f"summary {i}",
        datetime(2000, 2, i),
        f"poster {i}",
        [f"genre {i}",],
        float(i)
    ) for i in range(1, 9)]

    @staticmethod
    def create_movie_repository() -> MovieRepository:
        repository = Mock(spec=MovieRepository)
        return repository

    @staticmethod
    def set_return_value(
        repository: Mock,
        filter_tags: list[str] | None = None,
        min_rating: float = 0
    ) -> None:
        movie_list = []
        if filter_tags:
            movie_list = [
                movie for movie in MovieRepositoryFixture.movies
                if str(movie.genre) in filter_tags and float(movie.vote_average) > min_rating
            ]
        else:
            movie_list = [
                movie for movie in MovieRepositoryFixture.movies
                if float(movie.vote_average) > min_rating
            ]

        repository.list_movies.return_value = {
            "movies": movie_list,
            "total_pages": 1
        }
