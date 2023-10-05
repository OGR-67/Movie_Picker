from domain.entities.watchlist_item import WatchlistItem
from tests.custom_test_case import CustomTestCase
from tests.integration.test_utils.commons.db_connection_test import \
    create_test_app, \
    rollback_and_close_db_connection
from tests.integration.test_utils.movies.helpers import \
    given_a_movie_in_db, \
    given_a_movie_repository
from tests.integration.test_utils.users.helpers import \
    given_a_user_in_db, \
    given_a_user_repository, \
    when_add_user
from tests.integration.test_utils.watchlist.helpers import \
    given_a_watchlist_repository, \
    then_item_is_added, \
    then_watchlist_is_found, \
    when_adding_item, \
    when_get_watchlist, \
    when_removing_item


class TestFavoriteRepositoryIntegration(CustomTestCase):
    def setUp(self) -> None:
        # Given
        self.db_conn, self.app = create_test_app()
        self.watchlist_repository = given_a_watchlist_repository(self.db_conn)
        self.user_repository = given_a_user_repository(self.db_conn)
        self.movie_repository = given_a_movie_repository(self.db_conn)

    def tearDown(self) -> None:
        rollback_and_close_db_connection(self.db_conn)

    def test_get_watchlist_empty(self) -> None:
        # Given
        expected_items: list[WatchlistItem] = []
        valid_username = "username"
        valid_password = "password"

        # When
        user = when_add_user(self, valid_username, valid_password)
        empty_watchlist = when_get_watchlist(self, user.id)

        # Then
        then_watchlist_is_found(
            self, empty_watchlist, expected_items)

    def test_add_item(self) -> None:
        # Given
        movie = given_a_movie_in_db(self.db_conn)
        user = given_a_user_in_db(self)
        expected_watchlist_item = WatchlistItem(
            id=1,
            user_id=user.id,
            movie_id=movie.id
        )

        # When
        item = when_adding_item(self, user.id, movie.id)

        # Then
        then_item_is_added(self, item, expected_watchlist_item)

    def test_get_watchlist(self) -> None:
        # Given
        movie = given_a_movie_in_db(self.db_conn)
        user = given_a_user_in_db(self)
        expected_watchlist_item = WatchlistItem(
            id=1,
            user_id=user.id,
            movie_id=movie.id
        )
        expected_watchlist = [expected_watchlist_item]

        # When
        when_adding_item(self, user.id, movie.id)
        watchlist = when_get_watchlist(self, user.id)

        # Then
        then_watchlist_is_found(
            self, watchlist, expected_watchlist)

    def test_get_watchlist_multiple(self) -> None:
        # Given
        movie1 = given_a_movie_in_db(self.db_conn)
        movie2 = given_a_movie_in_db(self.db_conn)
        user = given_a_user_in_db(self)
        expected_item1 = WatchlistItem(
            id=1,
            user_id=user.id,
            movie_id=movie1.id
        )
        expected_item2 = WatchlistItem(
            id=2,
            user_id=user.id,
            movie_id=movie2.id
        )
        expected_watchlist = [expected_item1, expected_item2]

        # When
        when_adding_item(self, user.id, movie1.id)
        when_adding_item(self, user.id, movie2.id)
        watchlist = when_get_watchlist(self, user.id)

        # Then
        then_watchlist_is_found(
            self, watchlist, expected_watchlist)

    def test_remove_an_item(self) -> None:
        # Given
        movie = given_a_movie_in_db(self.db_conn)
        user = given_a_user_in_db(self)
        expected_watchlist: list[WatchlistItem] = []

        # When
        when_adding_item(self, user.id, movie.id)
        when_removing_item(self, user.id, movie.id)
        watchlist = when_get_watchlist(self, user.id)

        # Then
        then_watchlist_is_found(
            self, watchlist, expected_watchlist)
