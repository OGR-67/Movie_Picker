from abc import ABC, abstractmethod
from domain.entities.favorite import Favorite
from domain.repositories.favorite_repository import FavoriteRepository


class FavoriteServiceInterface(ABC):
    def __init__(self, favorite_repository: FavoriteRepository) -> None:
        self.favorite_repository = favorite_repository

    @abstractmethod
    def get_favorites(self, user_id: int) -> list[Favorite]:
        pass

    @abstractmethod
    def add_favorite(self, user_id: int, movie_id: int) -> Favorite:
        pass

    @abstractmethod
    def remove_favorite(self, user_id: int, movie_id: int) -> None:
        pass


class FavoriteService(FavoriteServiceInterface):
    def __init__(self, favorite_repository: FavoriteRepository) -> None:
        self.favorite_repository = favorite_repository

    def get_favorites(self, user_id: int) -> list[Favorite]:
        return self.favorite_repository.get_favorites(user_id)

    def add_favorite(self, user_id: int, movie_id: int) -> Favorite:
        return self.favorite_repository.add_favorite(user_id, movie_id)

    def remove_favorite(self, user_id: int, movie_id: int) -> None:
        self.favorite_repository.remove_favorite(user_id, movie_id)
