from domain.entities.movie import Movie
from domain.entities.watchlist_item import WatchlistItem
from domain.repositories.watchlist_repository import WatchlistRepository
from tests.unit.test_utils.movies.movie_repository_fixture import \
    MovieRepositoryFixture


class WatchlistRepositoryFixture(WatchlistRepository):
    def __init__(self) -> None:
        self._watchlist: list[WatchlistItem] = []

    def add_item(self, user_id: int, movie_id: int) -> WatchlistItem:
        id = len(self._watchlist) + 1
        item: WatchlistItem = WatchlistItem(id, user_id, movie_id)
        self._watchlist.append(item)
        return item

    def remove_item(self, user_id: int, movie_id: int) -> None:
        self._watchlist = list(filter(
            lambda item: item.user_id != user_id or item.movie_id != movie_id,
            self._watchlist
        ))

    def get_watchlist(self, user_id: int) -> list[WatchlistItem]:
        return list(filter(
            lambda item: item.user_id == user_id,
            self._watchlist
        ))

    def get_watchlist_movies(self, user_id: int) -> list[Movie]:
        return [MovieRepositoryFixture().movies[0]]
