from unittest import TestCase

from domain.repositories.movie_repository import MovieRepository
from domain.repositories.user_repository import UserRepository
from domain.services.movie_service import MovieServiceInterface
from domain.services.user_service import UserServiceInterface


class CustomTestCase(TestCase):
    movie_repository: MovieRepository
    movie_service: MovieServiceInterface

    user_repository: UserRepository
    user_service: UserServiceInterface
