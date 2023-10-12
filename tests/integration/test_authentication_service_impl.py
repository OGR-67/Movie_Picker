from tests.custom_test_case import CustomTestCase
from tests.integration.test_utils.authentication.helpers import \
    when_check_is_logged_in, \
    when_login
from tests.integration.test_utils.commons.db_connection_test import \
    create_test_app, \
    rollback_and_close_db_connection
from tests.integration.test_utils.users.helpers import given_a_user_repository
from adapters.authentication_service_impl import AuthenticationServiceImpl
from tests.unit.test_utils.users.helpers import given_a_user_service


class TestAuthenticationServiceIntegration(CustomTestCase):
    def setUp(self) -> None:
        # Given
        self.db_conn, self.app = create_test_app()
        self.user_repository = given_a_user_repository(self.db_conn)
        self.user_service = given_a_user_service(self)
        self.authentication_service = AuthenticationServiceImpl(
            self.user_service
        )

    def tearDown(self) -> None:
        rollback_and_close_db_connection(self.db_conn)

    def test_is_logged_in_when_not_logged_in(self) -> None:
        with self.app.test_request_context():
            # When
            is_logged_in = self.authentication_service.is_logged_in()

            # Then
            self.assertFalse(is_logged_in)

    def test_is_logged_in_when_logged_in(self) -> None:
        # Given
        user = self.user_service.register("username", "password")

        with self.app.test_request_context():

            # When
            when_login(self, user.username, "password")
            is_logged_in = when_check_is_logged_in(self)

            # Then
            self.assertTrue(is_logged_in)
