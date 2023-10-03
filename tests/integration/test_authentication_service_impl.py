from tests.custom_test_case import CustomTestCase
from tests.integration.test_utils.commons.db_connection_test import \
    create_test_app, \
    rollback_and_close_db_connection
from tests.integration.test_utils.users.helpers import given_a_user_repository
from adapters.authentication_service_impl import AuthenticationServiceImpl
from domain.services.user_service import UserService


class TestAuthenticationServiceIntegration(CustomTestCase):
    def setUp(self) -> None:
        # Given
        self.db_conn, self.app = create_test_app()
        self.user_repository = given_a_user_repository(self.db_conn)
        self.user_service = UserService(self.user_repository)

    def tearDown(self) -> None:
        rollback_and_close_db_connection(self.db_conn)

    def test_is_logged_in_when_not_logged_in(self) -> None:
        with self.app.test_request_context():
            # Given
            authentication_service = AuthenticationServiceImpl(
                self.user_service
            )
            # When
            is_logged_in = authentication_service.is_logged_in()

            # Then
            self.assertFalse(is_logged_in)

    def test_is_logged_in_when_logged_in(self) -> None:
        with self.app.test_request_context():
            # Given
            user = self.user_service.register("username", "password")
            authentication_service = AuthenticationServiceImpl(
                self.user_service
            )
            authentication_service.login(user.username, "password")

            # When
            is_logged_in = authentication_service.is_logged_in()

            # Then
            self.assertTrue(is_logged_in)
