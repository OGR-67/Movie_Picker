import unittest
import sqlite3
from adapters.movie_repository_impl import MovieRepositoryImpl
from domain.entities.movie import Movie
from paths import DB_PATH
from tests.custom_test_case import CustomTestCase
from tests.integration.test_utils.movies.helpers import given_a_db_connection, given_a_movie_repository, rollback_and_close_db_connection, then_movie_is_found, then_movie_is_not_found, then_movies_are_filtered, then_movies_are_found, when_get_movie_by_id, when_get_movies


class TestMovieRepositoryIntegration_Get_Movie(CustomTestCase):
    def setUp(self) -> None:
        # Given
        self.db_conn = given_a_db_connection()
        self.movie_repository = given_a_movie_repository()

    def tearDown(self) -> None:
        rollback_and_close_db_connection(self.db_conn)

    def test_get_movie_nonexistent(self) -> None:
        # When
        inexistent_movie_id = -1
        nonexistent_movie = when_get_movie_by_id(self, inexistent_movie_id)

        # Then
        then_movie_is_not_found(nonexistent_movie)

    def test_get_movie_existent(self) -> None:
        # Given
        existent_movie_id = 1
        properties_to_check = {
            "id": int,
            "title": str,
            "original_language": str,
            "summary": str,
            "release_date": str,
            "poster_url": str,
            "genre": list,
            "vote_average": float
        }

        # When
        existent_movie = when_get_movie_by_id(self, existent_movie_id)

        # Then
        then_movie_is_found(
            self, existent_movie,
            existent_movie_id,
            properties_to_check
        )


class TestMovieRepositoryIntegration_Get_Movies(CustomTestCase):
    def setUp(self) -> None:
        # Given
        self.db_conn = given_a_db_connection()
        self.movie_repository = given_a_movie_repository()

    def tearDown(self) -> None:
        rollback_and_close_db_connection(self.db_conn)

    def test_get_movies_no_filter(self) -> None:
        # Given
        filter_tags = None
        min_rating = 0.0

        # When
        results = when_get_movies(self, filter_tags, min_rating)

        # Then
        then_movies_are_found(self, results)

    def test_get_movies_filtered_by_ratings(self) -> None:
        # Given
        min_rating = 5

        # When
        non_filtered_results = when_get_movies(
            self, filter_tags=None, min_rating=0.0)
        filtered_results = when_get_movies(
            self, filter_tags=None, min_rating=min_rating)

        # Then
        then_movies_are_found(self, non_filtered_results)
        then_movies_are_found(self, filtered_results)
        then_movies_are_filtered(
            self,
            filtered_results,
            non_filtered_results
        )


if __name__ == '__main__':
    unittest.main()
