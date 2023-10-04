from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from domain.services.user_service import UserService, UserServiceInterface
from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.users.user_repository_fixture import\
    UserRepositoryFixture


def given_a_user_repository() -> UserRepository:
    return UserRepositoryFixture()


def given_a_user_service(test_case: CustomTestCase) -> UserServiceInterface:
    return UserService(test_case.user_repository)


def when_register(
    user_service: UserServiceInterface,
    username: str,
    password: str
) -> User:
    return user_service.register(username, password)


def then_user_is_registered(
    test_case: CustomTestCase,
    user: User,
    username: str,
    password: str
) -> None:
    test_case.assertIsNotNone(user.id)
    test_case.assertEqual(user.username, username)
    test_case.assertEqual(
        user.password, test_case.user_service.hash_password(password))


def then_error_message_is_username_already_exists(
    test_case: CustomTestCase,
    exception: Exception
) -> None:
    test_case.assertEqual(str(exception), 'Username already exists')


def then_error_message_is_password_too_short(
    test_case: CustomTestCase,
    exception: Exception
) -> None:
    test_case.assertEqual(str(exception), 'Password too short')


def then_error_message_is_username_too_short(
    test_case: CustomTestCase,
    exception: Exception
) -> None:
    test_case.assertEqual(str(exception), 'Username too short')


def then_error_message_is_username_cannot_contain_spaces(
    test_case: CustomTestCase,
    exception: Exception
) -> None:
    test_case.assertEqual(str(exception), 'Username cannot contain spaces')


def then_error_message_is_username_or_password_incorrect(
    test_case: CustomTestCase,
    exception: Exception
) -> None:
    test_case.assertEqual(str(exception), 'username or password is incorrect')


def then_user_is_logged_in(
    test_case: CustomTestCase,
    user: User,
    username: str,
    password: str
) -> None:
    test_case.assertIsNotNone(user.id)
    test_case.assertEqual(user.username, username)
    test_case.assertEqual(
        user.password, test_case.user_service.hash_password(password))
