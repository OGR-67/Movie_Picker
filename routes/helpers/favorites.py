from adapters.db_connection import get_thread_db
from adapters.favorite_repository_impl import FavoriteRepositoryImpl
from domain.entities.movie import Movie


def get_favorite_movies(user_id: int) -> list[Movie]:
    favorite_repository = FavoriteRepositoryImpl(get_thread_db())
    favorite_movies = favorite_repository.get_favorite_movies(user_id)
    return favorite_movies
