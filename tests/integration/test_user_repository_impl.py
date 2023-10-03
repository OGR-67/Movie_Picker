from tests.custom_test_case import CustomTestCase
from tests.integration.test_utils.commons.db_connection_test import \
    create_test_app, \
    rollback_and_close_db_connection
from tests.integration.test_utils.users.helpers import\
    given_a_user_repository, \
    then_user_is_not_loggedIn, \
    then_user_is_loggedIn, \
    then_user_is_registered, \
    then_users_are_found, \
    when_add_user, \
    when_get_users


class TestUserRepositoryIntegration(CustomTestCase):
    def setUp(self) -> None:
        # Given
        self.db_conn, self.app = create_test_app()
        self.user_repository = given_a_user_repository(self.db_conn)

    def tearDown(self) -> None:
        rollback_and_close_db_connection(self.db_conn)

    def test_get_users(self) -> None:
        # When
        users = when_get_users(self)

        # Then
        then_users_are_found(self, users)

    def test_add_user(self) -> None:
        # Given
        valid_username = "username"
        valid_password = "password"

        # When
        user = when_add_user(self, valid_username, valid_password)

        # Then
        then_user_is_registered(self, user, valid_username, valid_password)

    def test_login_with_valid_credentials(self) -> None:
        # Given
        valid_username = "username"
        valid_password = "password"
        when_add_user(self, valid_username, valid_password)

        # When
        user = self.user_repository.check_credentials(
            valid_username,
            valid_password
        )

        # Then
        then_user_is_loggedIn(self, user, valid_username, valid_password)

    def test_login_with_invalid_credentials(self) -> None:
        # Given
        valid_username = "username"
        valid_password = "password"
        when_add_user(self, valid_username, valid_password)

        # When
        user = self.user_repository.check_credentials(
            valid_username,
            "invalid_password"
        )

        # Then
        then_user_is_not_loggedIn(self, user)
