from typing import Any
from unittest.mock import Mock
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository
from domain.services.movie_service import MovieService
from tests.unit.test_utils.movies.movie_repository_fixture import MovieRepositoryFixture


class MovieServiceMock(MovieService):
    def __init__(self, movie_repository: MovieRepository):
        super().__init__(movie_repository)
        self.results: dict[str, Any] = {
            "movies": [],
            "total_pages": 1
        }
        self.result: Movie | None = None

    def get_movies(
        self,
        page: int,
        filter_tags: list[str] | None = None,
        min_rating: float = 0.0
    ) -> dict[str, Any]:
        # We're using mocks in this test, which can lead to type checking errors.
        # Ignoring type here to suppress those errors since we're not testing
        # type correctness in this specific context.
        MovieRepositoryFixture.set_get_movies_return_value(
            self.movie_repository,  # type: ignore
            filter_tags=filter_tags,
            min_rating=min_rating
        )
        self.results = self.movie_repository.list_movies(
            page, filter_tags, min_rating)
        return self.results

    def get_movie_by_id(
        self,
        movie_id: int
    ) -> Movie:
        # We're using mocks in this test, which can lead to type checking errors.
        # Ignoring type here to suppress those errors since we're not testing
        # type correctness in this specific context.
        MovieRepositoryFixture.set_get_movie_return_value(
            self.movie_repository,  # type: ignore
            movie_id=movie_id
        )
        self.result = self.movie_repository.get_movie(movie_id)
        return self.result
