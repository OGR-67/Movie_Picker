from tests.unit.test_utils.movies.movie_repository_fixture import MovieRepositoryFixture
from tests.unit.test_utils.movies.movie_service_stub import MovieServiceMock


def given_a_movie_repository(test_case):
    test_case.movie_repository = MovieRepositoryFixture.create_movie_repository()


def given_a_movie_service(test_case):
    test_case.movie_service = MovieServiceMock(
        test_case.movie_repository
    )


def when_get_movies(test_case, filter_tags=None):
    test_case.movie_service.get_movies(page=1, filter_tags=filter_tags)


def then_movie_repository_list_movies_was_called_with(test_case, page, filter_tags):
    test_case.movie_repository.list_movies.assert_called_once_with(
        page,
        filter_tags
    )


def then_result_equals_expected_movies(test_case, expected_movies):
    test_case.assertEqual(
        test_case.movie_service.results["movies"], expected_movies
    )
