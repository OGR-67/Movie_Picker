from sqlite3 import Connection
from adapters.user_repository_impl import UserRepositoryImpl
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from domain.services.user_service import UserService
from tests.custom_test_case import CustomTestCase


def given_a_user_repository(db_conn: Connection) -> UserRepository:
    return UserRepositoryImpl(db_conn)


def given_a_user_in_db(test_case: CustomTestCase) -> User:
    user_service = UserService(test_case.user_repository)
    user = user_service.register("unused_username", "password")
    return user


def when_get_users(test_case: CustomTestCase) -> list[User]:
    return test_case.user_repository.get_users()


def then_users_are_found(test_case: CustomTestCase, users: list[User]) -> None:
    test_case.assertIsInstance(users, list)
    test_case.assertGreaterEqual(len(users), 0)
    for user in users:
        test_case.assertIsInstance(user, User)


def when_add_user(
    test_case: CustomTestCase,
    username: str,
    password: str
) -> User:
    return test_case.user_repository.add_user(username, password)


def then_user_is_registered(
    test_case: CustomTestCase,
    user: User,
    username: str,
    password: str
) -> None:
    test_case.assertIsNotNone(user.id)
    test_case.assertGreaterEqual(user.id, 1)
    test_case.assertEqual(user.username, username)
    test_case.assertEqual(user.password, password)


def then_user_is_loggedIn(
    test_case: CustomTestCase,
    user: User | None,
    username: str,
    password: str
) -> None:
    test_case.assertIsNotNone(user)
    test_case.assertIsInstance(user, User)
    assert isinstance(user, User)  # for mypy
    test_case.assertEqual(user.username, username)
    test_case.assertEqual(user.password, password)


def then_user_is_not_loggedIn(
    test_case: CustomTestCase,
    user: User | None,
) -> None:
    test_case.assertIsNone(user)
