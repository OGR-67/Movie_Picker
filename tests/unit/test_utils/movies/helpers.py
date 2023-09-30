from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository
from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.movies.movie_repository_fixture import MovieRepositoryFixture
from tests.unit.test_utils.movies.movie_service_stub import MovieServiceMock
from unittest.mock import Mock


def given_a_movie_repository(
    test_case: CustomTestCase
) -> None:
    test_case.movie_repository = MovieRepositoryFixture.create_movie_repository()


def given_a_movie_service(
    test_case: CustomTestCase
) -> None:
    test_case.movie_service = MovieServiceMock(
        test_case.movie_repository
    )


def when_get_movies(
    test_case: CustomTestCase,
    filter_tags: list[str] | None = None,
    min_rating: float = 0.0
) -> None:
    test_case.movie_service.get_movies(
        page=1, filter_tags=filter_tags, min_rating=min_rating)


def then_movie_repository_list_movies_was_called_with(
    test_case: CustomTestCase,
    page: int,
    filter_tags: list[str] | None = None,
    min_rating: float = 0.0
) -> None:
    # We're using mocks in this test, which can lead to type checking errors.
    # Ignoring type here to suppress those errors since we're not testing
    # type correctness in this specific context.
    test_case.movie_repository.list_movies.assert_called_once_with(  # type: ignore
        page,
        filter_tags,
        min_rating
    )


def then_result_equals_expected_movies(
    test_case: CustomTestCase,
    expected_movies: list[Movie]
) -> None:
    test_case.assertEqual(
        test_case.movie_service.results["movies"], expected_movies
    )
