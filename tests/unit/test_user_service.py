from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.users.helpers import \
    given_a_user_repository, \
    given_a_user_service, \
    then_error_message_is_password_too_short, \
    then_error_message_is_username_already_exists, \
    then_error_message_is_username_cannot_contain_spaces, \
    then_error_message_is_username_too_short, \
    then_user_is_registered, \
    when_register


class TestRegister(CustomTestCase):
    def setUp(self) -> None:
        self.user_repository = given_a_user_repository()
        self.user_service = given_a_user_service(self)

    def test_register(self: CustomTestCase) -> None:
        # Given
        username = 'user1'
        password = 'password 1'

        # When
        user = when_register(self.user_service, username, password)

        # Then
        then_user_is_registered(self, user, username, password)

    def test_register_with_existing_username(self: CustomTestCase) -> None:
        # Given
        username = 'user1'
        password = 'password 1'

        # When
        when_register(self.user_service, username, password)
        with self.assertRaises(Exception) as context:
            when_register(self.user_service, username, password)

        # Then
        then_error_message_is_username_already_exists(self, context.exception)

    def test_register_with_username_too_short(self: CustomTestCase) -> None:
        # Given
        username = 'u'
        password = 'password 1'

        # When
        with self.assertRaises(Exception) as context:
            when_register(self.user_service, username, password)

        # Then
        then_error_message_is_username_too_short(self, context.exception)

    def test_register_with_space_in_username(self: CustomTestCase) -> None:
        # Given
        username = 'user 1'
        password = 'password 1'

        # When
        with self.assertRaises(Exception) as context:
            when_register(self.user_service, username, password)

        # Then
        then_error_message_is_username_cannot_contain_spaces(
            self, context.exception)

    def test_register_with_short_password(self: CustomTestCase) -> None:
        # Given
        username = 'user1'
        password = '1234567'

        # When
        with self.assertRaises(Exception) as context:
            when_register(self.user_service, username, password)

        # Then
        then_error_message_is_password_too_short(self, context.exception)
