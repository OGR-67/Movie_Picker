from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.users.helpers import \
    given_a_user_repository, \
    given_a_user_service, \
    then_error_message_is, \
    then_user_is_logged_in, \
    then_user_is_registered, \
    then_user_table_is_empty, \
    when_delete_user, \
    when_register, \
    when_user_login


class TestRegister(CustomTestCase):
    def setUp(self) -> None:
        self.user_repository = given_a_user_repository()
        self.user_service = given_a_user_service(self)

    def test_register(self: CustomTestCase) -> None:
        # Given
        username = 'user'
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
        then_error_message_is(self, context.exception,
                              "Username already exists")

    def test_register_with_username_too_short(self: CustomTestCase) -> None:
        # Given
        username = 'u'
        password = 'password 1'

        # When
        with self.assertRaises(Exception) as context:
            when_register(self.user_service, username, password)

        # Then
        then_error_message_is(self, context.exception, "Username too short")

    def test_register_with_username_still_too_short(
        self: CustomTestCase
    ) -> None:
        # Given
        username = 'usr'
        password = 'password 1'

        # When
        with self.assertRaises(Exception) as context:
            when_register(self.user_service, username, password)

        # Then
        then_error_message_is(self, context.exception, "Username too short")

    def test_register_with_space_in_username(self: CustomTestCase) -> None:
        # Given
        username = 'user 1'
        password = 'password 1'

        # When
        with self.assertRaises(Exception) as context:
            when_register(self.user_service, username, password)

        # Then
        then_error_message_is(
            self, context.exception, "Username cannot contain spaces")

    def test_register_with_short_password(self: CustomTestCase) -> None:
        # Given
        username = 'user1'
        password = '1234567'

        # When
        with self.assertRaises(Exception) as context:
            when_register(self.user_service, username, password)

        # Then
        then_error_message_is(self, context.exception, 'Password too short')


class TestLogin(CustomTestCase):
    def setUp(self) -> None:
        self.user_repository = given_a_user_repository()
        self.user_service = given_a_user_service(self)

    def test_login_with_unregistered_user(self: CustomTestCase) -> None:
        # Given
        username = 'user1'
        password = 'password 1'

        # When
        with self.assertRaises(Exception) as context:
            self.user_service.login(username, password)

        # Then
        then_error_message_is(
            self, context.exception, 'username or password is incorrect')

    def test_login_with_registered_user_wrong_credentials(
        self: CustomTestCase
    ) -> None:
        # Given
        username = 'user1'
        password = 'password 1'
        when_register(self.user_service, username, password)

        # When
        with self.assertRaises(Exception) as context:
            self.user_service.login(username, 'wrong password')

        # Then
        then_error_message_is(
            self, context.exception, 'username or password is incorrect')

    def test_login_with_registered_user_correct_credentials(
        self: CustomTestCase
    ) -> None:
        # Given
        username = 'user1'
        password = 'password 1'
        when_register(self.user_service, username, password)

        # When
        user = when_user_login(self.user_service, username, password)

        # Then
        assert user is not None
        then_user_is_logged_in(self, user, username, password)


class TestDeleteProfile(CustomTestCase):
    def setUp(self) -> None:
        self.user_repository = given_a_user_repository()
        self.user_service = given_a_user_service(self)

    def test_delete_profile(self: CustomTestCase) -> None:
        # Given
        username = 'user1'
        password = 'password 1'
        user = when_register(self.user_service, username, password)

        # When
        when_delete_user(self, user.id)

        # Then
        then_user_table_is_empty(self)

    def test_delete_profile_user_not_found(self: CustomTestCase) -> None:
        # Given
        user_id = 1

        # When
        with self.assertRaises(Exception) as context:
            when_delete_user(self, user_id)

        # Then
        then_user_table_is_empty(self)
        then_error_message_is(self, context.exception, "User not found")
