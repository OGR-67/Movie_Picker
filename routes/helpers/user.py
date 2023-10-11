from flask import session
from adapters.authentication_service_impl import \
    AuthUser, \
    AuthenticationServiceImpl
from adapters.db_connection import get_thread_db
from adapters.favorite_repository_impl import FavoriteRepositoryImpl
from adapters.user_repository_impl import UserRepositoryImpl
from adapters.watchlist_repository_impl import WatchlistRepositoryImpl
from domain.entities.favorite import Favorite
from domain.entities.watchlist_item import WatchlistItem
from domain.services.favorite_service import FavoriteService
from domain.services.user_service import UserService
from domain.services.watchlist_service import WatchlistService


def get_user_infos(
) -> tuple[str | None, int | None, list[Favorite], list[WatchlistItem]]:
    user_repository = UserRepositoryImpl(get_thread_db())
    user_service = UserService(user_repository)
    authentication_service = AuthenticationServiceImpl(
        user_service
    )
    if authentication_service.is_logged_in():
        username: str | None = session["movie_picker_user"]["username"]
        user_id_str: str | None = session["movie_picker_user"]["id"]
        user_id: int | None = int(
            user_id_str) if user_id_str is not None else -1
        assert user_id is not None  # for mypy

        favorite_repository = FavoriteRepositoryImpl(get_thread_db())
        favorite_service = FavoriteService(favorite_repository)
        favorite_movies: list[Favorite] = favorite_service.get_favorites(
            user_id)

        watchlist_repository = WatchlistRepositoryImpl(get_thread_db())
        watchlist_service = WatchlistService(watchlist_repository)
        watchlist_movies: list[WatchlistItem] = watchlist_service\
            .get_watchlist(user_id)
    else:
        user_id = None
        username = None
        favorite_movies = []
        watchlist_movies = []
    return username, user_id, favorite_movies, watchlist_movies


def get_user_id(
) -> int:
    user: AuthUser = session["movie_picker_user"]
    return user["id"]
