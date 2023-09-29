from domain.services.movie_service import MovieService
from tests.unit.test_utils.movies.movie_repository_fixture import MovieRepositoryFixture


class MovieServiceMock(MovieService):
    def __init__(self, movie_repository):
        super().__init__(movie_repository)
        self.results = {"movies": [], "total_pages": 0}

    def get_movies(self, page: int, filter_tags=None, min_rating=0) -> dict:
        MovieRepositoryFixture.set_return_value(
            self.movie_repository,
            filter_tags=filter_tags,
            min_rating=min_rating
        )
        self.results = self.movie_repository.list_movies(
            page, filter_tags, min_rating)
