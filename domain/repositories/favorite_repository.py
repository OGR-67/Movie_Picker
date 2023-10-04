from abc import ABC, abstractmethod
from domain.entities.favorite import Favorite


class FavoriteRepository(ABC):

    @abstractmethod
    def get_favorites(self, user_id: int) -> list[Favorite]:
        pass

    @abstractmethod
    def add_favorite(self, user_id: int, movie_id: int) -> Favorite:
        pass

    @abstractmethod
    def remove_favorite(self, user_id: int, movie_id: int) -> None:
        pass
