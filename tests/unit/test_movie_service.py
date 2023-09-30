import unittest
from tests.unit.test_utils.movies.movie_repository_fixture import MovieRepositoryFixture
from tests.unit.test_utils.movies.movie_service_stub import MovieServiceMock
from tests.unit.test_utils.movies.helpers import given_a_movie_repository, given_a_movie_service, then_movie_repository_list_movies_was_called_with, then_result_equals_expected_movies, when_get_movies


class TestGetMovies(unittest.TestCase):
    def setUp(self):
        given_a_movie_repository(self)
        given_a_movie_service(self)

    def test_get_movies(self):
        # Given
        expected_movies = MovieRepositoryFixture.movies

        when_get_movies(self, filter_tags=None, min_rating=0)

        then_movie_repository_list_movies_was_called_with(
            self, page=1,
            filter_tags=None,
            min_rating=0
        )
        then_result_equals_expected_movies(self, expected_movies)

    def test_get_movies_with_filter_tags(self):
        # Given
        filter_tags = ['genre 1', 'genre 2']
        expected_movies = [
            movie for movie in MovieRepositoryFixture.movies if movie.genre in filter_tags]

        when_get_movies(self, filter_tags)

        then_movie_repository_list_movies_was_called_with(
            self, page=1, filter_tags=filter_tags
        )
        then_result_equals_expected_movies(self, expected_movies)

    def test_get_movies_with_wrong_filter_tags(self):
        # Given
        filter_tags = ['wrong 3', 'wrong 4']
        expected_movies = []

        when_get_movies(self, filter_tags)

        then_movie_repository_list_movies_was_called_with(
            self, page=1, filter_tags=filter_tags
        )
        then_result_equals_expected_movies(self, expected_movies)

    def test_get_movies_filtered_by_ratings(self):
        # Given
        min_rating = 5
        expected_movies = [
            movie for movie in MovieRepositoryFixture.movies if float(movie.vote_average) > min_rating
        ]

        when_get_movies(self, filter_tags=None, min_rating=min_rating)

        then_movie_repository_list_movies_was_called_with(
            self, page=1, filter_tags=None, min_rating=min_rating
        )
        then_result_equals_expected_movies(self, expected_movies)

    def test_get_movies_filtered_by_ratings_and_tags(self):
        # Given
        min_rating = 5
        filter_tags = ['genre 1', 'genre 2']
        expected_movies = [
            movie for movie in MovieRepositoryFixture.movies if float(movie.vote_average) > min_rating and movie.genre in filter_tags
        ]

        when_get_movies(self, filter_tags=filter_tags, min_rating=min_rating)

        then_movie_repository_list_movies_was_called_with(
            self, page=1, filter_tags=filter_tags, min_rating=min_rating
        )
        then_result_equals_expected_movies(self, expected_movies)

    def test_get_movies_filtered_by_ratings_and_wrong_tags(self):
        # Given
        min_rating = 5
        filter_tags = ['wrong 3', 'wrong 4']
        expected_movies = []

        when_get_movies(self, filter_tags=filter_tags, min_rating=min_rating)

        then_movie_repository_list_movies_was_called_with(
            self, page=1, filter_tags=filter_tags, min_rating=min_rating
        )
        then_result_equals_expected_movies(self, expected_movies)


if __name__ == '__main__':
    unittest.main()
