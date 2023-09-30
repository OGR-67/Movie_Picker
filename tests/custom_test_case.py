from unittest import TestCase

from domain.repositories.movie_repository import MovieRepository
from domain.services.movie_service import MovieService
from tests.unit.test_utils.movies.movie_repository_fixture import MovieRepositoryFixture
from tests.unit.test_utils.movies.movie_service_stub import MovieServiceMock


class CustomTestCase(TestCase):
    movie_repository: MovieRepository
    movie_service: MovieServiceMock
