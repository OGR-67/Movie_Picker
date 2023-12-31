from abc import ABC, abstractmethod
from domain.entities.movie import Movie
from typing import Any


class MovieRepository(ABC):

    @abstractmethod
    def get_movie(self, movie_id: int) -> Movie | None:
        pass

    @abstractmethod
    def list_movies(
        self,
        page: int,
        filter_tags: list[str] | None = None,
        min_rating: float = 0
    ) -> dict[str, Any]:
        pass
