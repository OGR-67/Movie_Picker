from domain.entities.favorite import Favorite
from domain.entities.movie import Movie
from domain.repositories.favorite_repository import FavoriteRepository
from domain.services.favorite_service import \
    FavoriteService, \
    FavoriteServiceInterface
from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.favorites.favorite_repository_fixture import \
    FavoriteRepositoryFixture


def given_a_favorite_repository() -> FavoriteRepository:
    return FavoriteRepositoryFixture()


def given_a_favorite_service(
    test_case: CustomTestCase
) -> FavoriteServiceInterface:
    return FavoriteService(test_case.favorite_repository)


def when_add_favorite(
    test_case: CustomTestCase,
    user_id: int,
    movie_id: int
) -> Favorite:
    return test_case.favorite_service.add_favorite(user_id, movie_id)


def when_get_favorites(
    test_case: CustomTestCase,
    user_id: int
) -> list[Favorite]:
    return test_case.favorite_service.get_favorites(user_id)


def when_get_favorite_movies(
    test_case: CustomTestCase,
    user_id: int
) -> list[Movie]:
    return test_case.favorite_service.get_favorite_movies(user_id)


def then_results_equals_expected_favorite(
    test_case: CustomTestCase,
    results: list[Favorite],
    expected_favorite: list[Favorite]
) -> None:
    test_case.assertEqual(results, expected_favorite)
