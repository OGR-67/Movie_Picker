from typing import Any
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository
from abc import ABC, abstractmethod


class MovieServiceInterface(ABC):
    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    @abstractmethod
    def get_movie_by_id(self, movie_id: int) -> Movie:
        pass

    @abstractmethod
    def get_movies(
        self,
        page: int,
        filter_tags: list[str] | None = None,
        min_rating: float = 0.0
    ) -> dict[str, Any]:
        pass


class MovieService(MovieServiceInterface):
    def __init__(self, movie_repository: MovieRepository):
        super().__init__(movie_repository)

    def get_movie_by_id(self, movie_id: int) -> Movie:
        return self.movie_repository.get_movie(movie_id)

    def get_movies(
        self,
        page: int,
        filter_tags: list[str] | None = None,
        min_rating: float = 0.0
    ) -> dict[str, Any]:
        """
        Retrieves a list of movies from the repository with pagination.

        Args:
            page (int): The page number to retrieve.
            filter_tags (list[str], optional): A list of tags to use as filters
                for selecting movies. Defaults to no filters applied.

        Returns:
            dict: A dictionary containing the list of movies and the total number of pages.
        """
        return self.movie_repository.list_movies(page, filter_tags=filter_tags, min_rating=min_rating)
