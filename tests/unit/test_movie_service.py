import unittest
from domain.entities.movie import Movie
from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.movies.movie_repository_fixture import MovieRepositoryFixture
from tests.unit.test_utils.movies.helpers import given_a_movie_repository, given_a_movie_service, given_a_set_of_movies, then_result_equals_expected_movie, then_results_equals_expected_movies, when_get_movie_by_id, when_get_movies


class TestGetMovies(CustomTestCase):

    def setUp(self) -> None:
        self.movie_repository = given_a_movie_repository()
        self.movie_service = given_a_movie_service(self)

    def test_get_movies(self) -> None:
        # Given
        expected_movies = given_a_set_of_movies()

        # When
        results = when_get_movies(self, filter_tags=None, min_rating=0)

        # Then
        then_results_equals_expected_movies(self, results, expected_movies)

    def test_get_movies_with_filter_tags(self) -> None:
        # Given
        filter_tags = ['genre 1', 'genre 2']
        movies_set = given_a_set_of_movies()
        expected_movies = [
            movie for movie in movies_set if str(movie.genre) in filter_tags]

        # When
        results = when_get_movies(self, filter_tags)

        # Then
        then_results_equals_expected_movies(self, results, expected_movies)

    def test_get_movies_with_wrong_filter_tags(self) -> None:
        # Given
        filter_tags = ['wrong 3', 'wrong 4']
        expected_movies: list[Movie] = []

        # When
        results = when_get_movies(self, filter_tags)

        # Then
        then_results_equals_expected_movies(self, results, expected_movies)

    def test_get_movies_filtered_by_ratings(self) -> None:
        # Given
        min_rating = 5
        movies_set = given_a_set_of_movies()
        expected_movies = [
            movie for movie in movies_set if float(movie.vote_average) > min_rating
        ]

        # When
        results = when_get_movies(
            self, filter_tags=None, min_rating=min_rating)

        # Then
        then_results_equals_expected_movies(self, results, expected_movies)

    def test_get_movies_filtered_by_ratings_and_tags(self) -> None:
        # Given
        min_rating = 5
        filter_tags = ['genre 1', 'genre 2']
        movies_set = given_a_set_of_movies()
        expected_movies = [
            movie for movie in movies_set if float(movie.vote_average) > min_rating and str(movie.genre) in filter_tags
        ]

        # When
        results = when_get_movies(
            self, filter_tags=filter_tags, min_rating=min_rating)

        # Then
        then_results_equals_expected_movies(self, results, expected_movies)

    def test_get_movies_filtered_by_ratings_and_wrong_tags(self) -> None:
        # Given
        min_rating = 5
        filter_tags = ['wrong 3', 'wrong 4']
        expected_movies: list[Movie] = []

        # When
        results = when_get_movies(
            self, filter_tags=filter_tags, min_rating=min_rating)

        # Then
        then_results_equals_expected_movies(self, results, expected_movies)


class TestGetMovieById(CustomTestCase):
    def setUp(self) -> None:
        self.movie_repository = given_a_movie_repository()
        self.movie_service = given_a_movie_service(self)

    def test_get_movie_with_valid_id(self) -> None:
        # Given
        movie_id = 1
        movies_set = given_a_set_of_movies()
        expected_movie = movies_set[movie_id - 1]

        # When
        result = when_get_movie_by_id(self, movie_id)

        # Then
        then_result_equals_expected_movie(self, result, expected_movie)

    def test_get_movie_with_invalid_id(self) -> None:
        # Given
        movie_id = 100
        expected_movie = None

        # When
        result = when_get_movie_by_id(self, movie_id)

        # Then
        then_result_equals_expected_movie(self, result, expected_movie)


if __name__ == '__main__':
    unittest.main()
