from adapters.db_connection import get_thread_db
from adapters.watchlist_repository_impl import WatchlistRepositoryImpl
from domain.entities.movie import Movie


def get_watchlist_movies(user_id: int) -> list[Movie]:
    watchlist_repository = WatchlistRepositoryImpl(get_thread_db())
    watchlist_movies = watchlist_repository.get_watchlist_movies(user_id)
    return watchlist_movies
