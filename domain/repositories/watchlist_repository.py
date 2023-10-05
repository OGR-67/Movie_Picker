from abc import ABC, abstractmethod
from domain.entities.watchlist_item import WatchlistItem


class WatchlistRepository(ABC):

    @abstractmethod
    def get_watchlist(self, user_id: int) -> list[WatchlistItem]:
        pass

    @abstractmethod
    def add_item(self, user_id: int, movie_id: int) -> WatchlistItem:
        pass

    @abstractmethod
    def remove_item(self, user_id: int, movie_id: int) -> None:
        pass
