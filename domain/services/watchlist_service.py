from abc import ABC, abstractmethod
from domain.entities.watchlist_item import WatchlistItem
from domain.repositories.watchlist_repository import WatchlistRepository


class WatchlistServiceInterface(ABC):
    def __init__(self, watchlist_repository: WatchlistRepository) -> None:
        self.watchlist_repository = watchlist_repository

    @abstractmethod
    def get_watchlist(self, user_id: int) -> list[WatchlistItem]:
        pass

    @abstractmethod
    def add_to_watchlist(self, user_id: int, movie_id: int) -> WatchlistItem:
        pass

    @abstractmethod
    def remove_from_watchlist(self, user_id: int, movie_id: int) -> None:
        pass


class WatchlistService(WatchlistServiceInterface):
    def __init__(self, watchlist_repository: WatchlistRepository) -> None:
        self.watchlist_repository = watchlist_repository

    def get_watchlist(self, user_id: int) -> list[WatchlistItem]:
        return self.watchlist_repository.get_watchlist(user_id)

    def add_to_watchlist(self, user_id: int, movie_id: int) -> WatchlistItem:
        return self.watchlist_repository.add_item(user_id, movie_id)

    def remove_from_watchlist(self, user_id: int, movie_id: int) -> None:
        self.watchlist_repository.remove_item(user_id, movie_id)
