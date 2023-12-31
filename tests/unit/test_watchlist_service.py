from domain.entities.watchlist_item import WatchlistItem
from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.movies.movie_repository_fixture import \
    MovieRepositoryFixture
from tests.unit.test_utils.watchlist.helpers import \
    given_a_watchlist_repository, \
    given_a_watchlist_service, \
    then_item_is_added, \
    then_watchlist_is, \
    when_add_item, \
    when_delete_item, \
    when_get_watchlist, \
    when_get_watchlist_movies


class TestWatchlistService(CustomTestCase):
    def setUp(self) -> None:
        self.watchlist_repository = given_a_watchlist_repository()
        self.watchlist_service = given_a_watchlist_service(self)

    def test_add_item(self: CustomTestCase) -> None:
        # Given
        user_id = 1
        movie_id = 1

        # When
        item = when_add_item(self, user_id, movie_id)

        # Then
        then_item_is_added(self, item, user_id, movie_id)

    def test_get_watchlist_empty(self: CustomTestCase) -> None:
        # Given
        user_id = 1
        expectedWatchlist: list[WatchlistItem] = []

        # When
        watchlist = when_get_watchlist(self, user_id)

        # Then
        then_watchlist_is(self, watchlist, expectedWatchlist)

    def test_get_watchlist_with_one_item(self: CustomTestCase) -> None:
        # Given
        user_id = 1
        movie_id = 1
        expectedWatchlist: list[WatchlistItem] = [
            WatchlistItem(1, user_id, movie_id)
        ]

        # When
        item = when_add_item(self, user_id, movie_id)
        watchlist = when_get_watchlist(self, user_id)

        # Then
        then_item_is_added(self, item, user_id, movie_id)
        then_watchlist_is(self, watchlist, expectedWatchlist)

    def test_get_watchlist_movies(self: CustomTestCase) -> None:
        # Given
        user_id = 1
        expected_movies = [MovieRepositoryFixture().movies[0]]

        # When
        movies = when_get_watchlist_movies(self, user_id)

        # Then
        assert movies == expected_movies

    def test_remove_item(self: CustomTestCase) -> None:
        # Given
        user_id = 1
        movie_id = 1
        expectedWatchlist: list[WatchlistItem] = []

        # When
        when_add_item(self, user_id, movie_id)
        when_delete_item(self, user_id, movie_id)
        watchlist = when_get_watchlist(self, user_id)

        # Then
        then_watchlist_is(self, watchlist, expectedWatchlist)
