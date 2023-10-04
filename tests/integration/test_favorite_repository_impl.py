from domain.entities.favorite import Favorite
from tests.custom_test_case import CustomTestCase
from tests.integration.test_utils.commons.db_connection_test import \
    create_test_app, rollback_and_close_db_connection
from tests.integration.test_utils.favorites.helpers import \
    given_a_favorite_repository, \
    then_favorite_is_added, \
    then_favorite_list_is_found, \
    when_adding_favorite, when_get_favorites, \
    when_removing_favorite
from tests.integration.test_utils.movies.helpers import \
    given_a_movie_in_db, \
    given_a_movie_repository
from tests.integration.test_utils.users.helpers import \
    given_a_user_in_db, \
    given_a_user_repository, \
    when_add_user


class TestFavoriteRepositoryIntegration_Get_Favorites(CustomTestCase):
    def setUp(self) -> None:
        # Given
        self.db_conn, self.app = create_test_app()
        self.favorite_repository = given_a_favorite_repository(self.db_conn)
        self.user_repository = given_a_user_repository(self.db_conn)
        self.movie_repository = given_a_movie_repository(self.db_conn)

    def tearDown(self) -> None:
        rollback_and_close_db_connection(self.db_conn)

    def test_get_favorites_no_favorites(self) -> None:
        # Given
        expected_favorites: list[Favorite] = []
        valid_username = "username"
        valid_password = "password"

        # When
        user = when_add_user(self, valid_username, valid_password)
        empty_favorite_list = when_get_favorites(self, user.id)

        # Then
        then_favorite_list_is_found(
            self, empty_favorite_list, expected_favorites)

    def test_add_favorite(self) -> None:
        # Given
        movie = given_a_movie_in_db(self.db_conn)
        user = given_a_user_in_db(self)
        expected_favorite = Favorite(
            id=1,
            user_id=user.id,
            movie_id=movie.id
        )

        # When
        favorite = when_adding_favorite(self, user.id, movie.id)

        # Then
        then_favorite_is_added(self, favorite, expected_favorite)

    def test_get_favorites(self) -> None:
        # Given
        movie = given_a_movie_in_db(self.db_conn)
        user = given_a_user_in_db(self)
        expected_favorite = Favorite(
            id=1,
            user_id=user.id,
            movie_id=movie.id
        )
        expected_favorites = [expected_favorite]

        # When
        when_adding_favorite(self, user.id, movie.id)
        favorite_list = when_get_favorites(self, user.id)

        # Then
        then_favorite_list_is_found(
            self, favorite_list, expected_favorites)

    def test_get_favorites_multiple(self) -> None:
        # Given
        movie1 = given_a_movie_in_db(self.db_conn)
        movie2 = given_a_movie_in_db(self.db_conn)
        user = given_a_user_in_db(self)
        expected_favorite1 = Favorite(
            id=1,
            user_id=user.id,
            movie_id=movie1.id
        )
        expected_favorite2 = Favorite(
            id=2,
            user_id=user.id,
            movie_id=movie2.id
        )
        expected_favorites = [expected_favorite1, expected_favorite2]

        # When
        when_adding_favorite(self, user.id, movie1.id)
        when_adding_favorite(self, user.id, movie2.id)
        favorite_list = when_get_favorites(self, user.id)

        # Then
        then_favorite_list_is_found(
            self, favorite_list, expected_favorites)

    def test_remove_a_favorite(self) -> None:
        # Given
        movie = given_a_movie_in_db(self.db_conn)
        user = given_a_user_in_db(self)
        expected_favorite_list: list[Favorite] = []

        # When
        when_adding_favorite(self, user.id, movie.id)
        when_removing_favorite(self, user.id, movie.id)
        favorite_list = when_get_favorites(self, user.id)

        # Then
        then_favorite_list_is_found(
            self, favorite_list, expected_favorite_list)
