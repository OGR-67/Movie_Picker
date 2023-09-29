from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository
from unittest.mock import Mock


class MovieRepositoryFixture:
    expected_movies = [Movie(
        i,
        f"title {i}",
        f"lang {i}",
        f"summary {i}",
        f"2000-02-0{i}",
        f"poster {i}",
        f"genre {i}",
        f"vote_average {i}"
    ) for i in range(1, 9)]

    @staticmethod
    def create_movie_repository():
        repository = Mock(spec=MovieRepository)
        return repository

    @staticmethod
    def set_return_value(repository, filter_tags=None):
        # TODO: implement tag filtering
        repository.list_movies.return_value = {
            "movies": MovieRepositoryFixture.expected_movies,
            "total_pages": 1
        }
