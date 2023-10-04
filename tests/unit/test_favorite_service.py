from domain.entities.favorite import Favorite
from tests.custom_test_case import CustomTestCase
from tests.unit.test_utils.favorites.helpers import \
    given_a_favorite_repository, \
    given_a_favorite_service, \
    then_results_equals_expected_favorite, \
    when_get_favorites


class TestGetFavoriteService(CustomTestCase):

    def setUp(self) -> None:
        self.favorite_repository = given_a_favorite_repository()
        self.favorite_service = given_a_favorite_service(self)

    def test_get_favorite_empty_list(self) -> None:
        # Given
        user_id = 1
        expected_favorite: list[Favorite] = []

        # When
        results = when_get_favorites(self, user_id)

        # Then
        then_results_equals_expected_favorite(self, results, expected_favorite)

    def test_add_favorite(self) -> None:
        # Given
        user_id = 1
        movie_id = 1
        expected_favorite = Favorite(
            1,
            user_id,
            movie_id
        )

        # When
        result = self.favorite_service.add_favorite(user_id, movie_id)

        # Then
        self.assertEqual(result, expected_favorite)

    def test_get_favorite(self) -> None:
        # Given
        user_id = 1
        movie_id = 1
        expected_favorite = Favorite(
            1,
            user_id,
            movie_id
        )
        self.favorite_service.add_favorite(user_id, movie_id)

        # When
        results = when_get_favorites(self, user_id)

        # Then
        then_results_equals_expected_favorite(
            self, results, [expected_favorite])

    def test_remove_favorite(self) -> None:
        # Given
        user_id = 1
        movie_id = 1
        self.favorite_service.add_favorite(user_id, movie_id)

        # When
        self.favorite_service.remove_favorite(user_id, movie_id)
        results = when_get_favorites(self, user_id)

        # Then
        then_results_equals_expected_favorite(
            self, results, expected_favorite=[])
