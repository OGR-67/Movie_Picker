import sqlite3
from adapters.favorite_repository_impl import FavoriteRepositoryImpl
from domain.entities.favorite import Favorite

from domain.repositories.favorite_repository import FavoriteRepository
from tests.custom_test_case import CustomTestCase


def given_a_favorite_repository(
    db_connect: sqlite3.Connection
) -> FavoriteRepository:
    return FavoriteRepositoryImpl(db_connect)


def when_get_favorites(
    test_case: CustomTestCase,
    user_id: int
) -> list[Favorite]:
    return test_case.favorite_repository.get_favorites(user_id)


def then_favorite_list_is_found(
    test_case: CustomTestCase,
    favorite_list: list[Favorite],
    expected_favorite_list: list[Favorite]
) -> None:
    test_case.assertEqual(len(favorite_list), len(expected_favorite_list))
    for i in range(len(favorite_list)):
        test_case.assertEqual(
            favorite_list[i].id, expected_favorite_list[i].id)
        test_case.assertEqual(
            favorite_list[i].user_id, expected_favorite_list[i].user_id)
        test_case.assertEqual(
            favorite_list[i].movie_id, expected_favorite_list[i].movie_id)


def when_adding_favorite(
    test_case: CustomTestCase,
    user_id: int,
    movie_id: int
) -> Favorite:
    return test_case.favorite_repository.add_favorite(user_id, movie_id)


def then_favorite_is_added(
    test_case: CustomTestCase,
    favorite: Favorite,
    expected_favorite: Favorite
) -> None:
    test_case.assertEqual(favorite.id, expected_favorite.id)
    test_case.assertEqual(favorite.user_id, expected_favorite.user_id)
    test_case.assertEqual(favorite.movie_id, expected_favorite.movie_id)


def when_removing_favorite(
    test_case: CustomTestCase,
    user_id: int,
    movie_id: int
) -> None:
    return test_case.favorite_repository.remove_favorite(user_id, movie_id)
