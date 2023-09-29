import unittest
from tests.unit.test_utils.movie_repository_fixture import MovieRepositoryFixture
from tests.unit.test_utils.movie_service_stub import MovieServiceMock
from tests.unit.test_utils.helpers import given_a_movie_repository, given_a_movie_service, then_movie_repository_list_movies_was_called_with, then_result_equals_expected_movies, when_get_movies


class TestMovieService(unittest.TestCase):
    def setUp(self):
        given_a_movie_repository(self)
        given_a_movie_service(self)

    def test_get_movies(self):

        when_get_movies(self, filter_tags=None)

        then_movie_repository_list_movies_was_called_with(
            self, page=1,
            filter_tags=None
        )
        then_result_equals_expected_movies(self)


if __name__ == '__main__':
    unittest.main()
