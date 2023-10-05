from sqlite3 import Connection
from adapters.watchlist_repository_impl import WatchlistRepositoryImpl
from domain.entities.watchlist_item import WatchlistItem
from domain.repositories.watchlist_repository import WatchlistRepository
from tests.custom_test_case import CustomTestCase


def given_a_watchlist_repository(db_conn: Connection) -> WatchlistRepository:
    return WatchlistRepositoryImpl(db_conn)


def when_get_watchlist(
    test_case: CustomTestCase, user_id: int
) -> list[WatchlistItem]:
    return test_case.watchlist_repository.get_watchlist(user_id)


def then_watchlist_is_found(
    test_case: CustomTestCase,
    watchlist: list[WatchlistItem],
    expected_items: list[WatchlistItem]
) -> None:
    test_case.assertEqual(len(watchlist), len(expected_items))
    for i in range(len(watchlist)):
        test_case.assertEqual(watchlist[i].id, expected_items[i].id)
        test_case.assertEqual(watchlist[i].user_id, expected_items[i].user_id)
        test_case.assertEqual(
            watchlist[i].movie_id, expected_items[i].movie_id)


def when_adding_item(
    test_case: CustomTestCase, user_id: int, movie_id: int
) -> WatchlistItem:
    return test_case.watchlist_repository.add_item(user_id, movie_id)


def then_item_is_added(
    test_case: CustomTestCase,
    item: WatchlistItem,
    expected_item: WatchlistItem
) -> None:
    test_case.assertEqual(item.id, expected_item.id)
    test_case.assertEqual(item.user_id, expected_item.user_id)
    test_case.assertEqual(item.movie_id, expected_item.movie_id)


def when_removing_item(
    test_case: CustomTestCase, user_id: int, movie_id: int
) -> None:
    test_case.watchlist_repository.remove_item(user_id, movie_id)
