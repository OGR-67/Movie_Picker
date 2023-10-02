import sqlite3
from typing import Any
from adapters.movie_repository_impl import MovieRepositoryImpl
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository
from paths import DB_PATH
from tests.custom_test_case import CustomTestCase


def given_a_db_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def rollback_and_close_db_connection(db_conn: sqlite3.Connection) -> None:
    db_conn.rollback()
    db_conn.close()


def given_a_movie_repository() -> MovieRepository:
    return MovieRepositoryImpl(DB_PATH)


def when_get_movie_by_id(
    test_case: CustomTestCase,
    movie_id: int
) -> Movie | None:
    return test_case.movie_repository.get_movie(movie_id)


def then_movie_is_not_found(movie: Movie | None) -> None:
    assert movie is None


def then_movie_is_found(
    test_case: CustomTestCase,
    movie: Movie | None,
    movie_id: int,
    properties_to_check: dict[str, type]
) -> None:
    assert movie is not None
    test_case.assertEqual(movie.id, movie_id)
    for property_name, property_type in properties_to_check.items():
        test_case.assertIsInstance(
            getattr(movie, property_name), property_type)


def when_get_movies(
    test_case: CustomTestCase,
    filter_tags: list[str] | None,
    min_rating: float
) -> dict[str, Any]:
    return test_case.movie_repository.list_movies(
        page=1,
        filter_tags=filter_tags,
        min_rating=min_rating
    )


def then_movies_are_found(
    test_case: CustomTestCase,
    results: dict[str, Any],
) -> None:
    test_case.assertIsInstance(results["movies"], list)
    test_case.assertGreater(len(results["movies"]), 0)
    for movie in results["movies"]:
        test_case.assertIsInstance(movie, Movie)
    test_case.assertIsInstance(results["total_pages"], int)


def then_movies_are_filtered(
    test_case: CustomTestCase,
    filtered_results: dict[str, Any],
    non_filtered_results: dict[str, Any]
) -> None:
    test_case.assertGreater(
        len(filtered_results["movies"]),
        0
    )
    test_case.assertGreater(
        len(non_filtered_results["movies"]),
        0
    )
    test_case.assertLess(
        filtered_results["total_pages"],
        non_filtered_results["total_pages"]
    )
