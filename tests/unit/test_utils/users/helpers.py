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


def when_user_login(
    user_service: UserServiceInterface,
    username: str,
    password: str
) -> User | None:
    return user_service.login(username, password)


def when_delete_user(
    test_case: CustomTestCase,
    user_id: int
) -> None:
    test_case.user_service.delete_profile(user_id)


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


def then_user_table_is_empty(
    test_case: CustomTestCase
) -> None:
    test_case.assertEqual(len(test_case.user_repository.get_users()), 0)


def then_error_message_is(
    test_case: CustomTestCase,
    exception: Exception,
    message: str
) -> None:
    test_case.assertEqual(str(exception), message)
