from domain.entities.favorite import Favorite
from domain.repositories.favorite_repository import FavoriteRepository


class FavoriteRepositoryFixture(FavoriteRepository):
    def __init__(self) -> None:
        self.favorites: list[Favorite] = []

    def get_favorites(self, user_id: int) -> list[Favorite]:
        return self.favorites

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
