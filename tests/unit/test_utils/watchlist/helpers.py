from domain.entities.watchlist_item import WatchlistItem
from domain.repositories.watchlist_repository import WatchlistRepository
from domain.services.watchlist_service import \
    WatchlistService, \
    WatchlistServiceInterface
from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.watchlist.watchlist_repository_fixture import \
    WatchlistRepositoryFixture


def given_a_watchlist_repository() -> WatchlistRepository:
    return WatchlistRepositoryFixture()


def given_a_watchlist_service(
    test_case: CustomTestCase
) -> WatchlistServiceInterface:
    return WatchlistService(
        test_case.watchlist_repository
    )


def when_add_item(
    test_case: CustomTestCase,
    user_id: int,
    movie_id: int
) -> WatchlistItem:
    return test_case.watchlist_service.add_to_watchlist(user_id, movie_id)


def then_item_is_added(
    test_case: CustomTestCase,
    item: WatchlistItem,
    user_id: int,
    movie_id: int
) -> None:
    assert item.user_id == user_id
    assert item.movie_id == movie_id
    assert item.id == 1


def then_watchlist_is(
    test_case: CustomTestCase,
    watchlist: list[WatchlistItem],
    expected_watchlist: list[WatchlistItem]
) -> None:
    assert watchlist == expected_watchlist
