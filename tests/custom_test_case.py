from unittest import TestCase
from domain.repositories.favorite_repository import FavoriteRepository
from domain.repositories.movie_repository import MovieRepository
from domain.repositories.user_repository import UserRepository
from domain.repositories.watchlist_repository import WatchlistRepository
from domain.services.authentication_service import AuthenticationService
from domain.services.favorite_service import FavoriteServiceInterface
from domain.services.movie_service import MovieServiceInterface
from domain.services.user_service import UserServiceInterface
from domain.services.watchlist_service import WatchlistServiceInterface


class CustomTestCase(TestCase):
    movie_repository: MovieRepository
    movie_service: MovieServiceInterface

    user_repository: UserRepository
    user_service: UserServiceInterface

    authentication_service: AuthenticationService

    favorite_repository: FavoriteRepository
    favorite_service: FavoriteServiceInterface

    watchlist_repository: WatchlistRepository
    watchlist_service: WatchlistServiceInterface
