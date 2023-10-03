from typing import Any
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository
from domain.services.movie_service import MovieService, MovieServiceInterface
from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.movies.movie_repository_fixture import\
    MovieRepositoryFixture


def given_a_movie_repository() -> MovieRepository:
    return MovieRepositoryFixture()


def given_a_movie_service(test_case: CustomTestCase) -> MovieServiceInterface:
    return MovieService(test_case.movie_repository)


def given_a_set_of_movies() -> list[Movie]:
    fixture = MovieRepositoryFixture()
    expected_movies = fixture.movies
    return expected_movies


def when_get_movies(
    test_case: CustomTestCase,
    filter_tags: list[str] | None = None,
    min_rating: float = 0.0
) -> dict[str, Any]:
    return test_case.movie_service.get_movies(
        page=1, filter_tags=filter_tags, min_rating=min_rating)


def then_results_equals_expected_movies(
    test_case: CustomTestCase,
    results: dict[str, Any],
    expected_movies: list[Movie]
) -> None:
    test_case.assertEqual(results["movies"], expected_movies)


def when_get_movie_by_id(
    test_case: CustomTestCase,
    movie_id: int
) -> Movie | None:
    return test_case.movie_service.get_movie_by_id(movie_id)


def then_result_equals_expected_movie(
    test_case: CustomTestCase,
    result: Movie | None,
    expected_movie: Movie | None
) -> None:
    test_case.assertEqual(result, expected_movie)
