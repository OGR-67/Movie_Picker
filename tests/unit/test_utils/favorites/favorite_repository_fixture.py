from domain.entities.favorite import Favorite
from domain.entities.movie import Movie
from domain.repositories.favorite_repository import FavoriteRepository
from tests.unit.test_utils.movies.movie_repository_fixture import \
    MovieRepositoryFixture


class FavoriteRepositoryFixture(FavoriteRepository):
    def __init__(self) -> None:
        self.favorites: list[Favorite] = []

    def get_favorites(self, user_id: int) -> list[Favorite]:
        return self.favorites

    def get_favorite_movies(self, user_id: int) -> list[Movie]:
        return [MovieRepositoryFixture().movies[0]]

    def add_favorite(self, user_id: int, movie_id: int) -> Favorite:
        favorite = Favorite(
            len(self.favorites) + 1,
            user_id,
            movie_id
        )
        self.favorites.append(favorite)
        return favorite

    def remove_favorite(self, user_id: int, movie_id: int) -> None:
        for favorite in self.favorites:
            if favorite.user_id == user_id and favorite.movie_id == movie_id:
                self.favorites.remove(favorite)
                return None
        raise Exception("Favorite not found")
