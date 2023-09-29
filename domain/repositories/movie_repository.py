from abc import ABC, abstractmethod
from domain.entities.movie import Movie


class MovieRepository(ABC):
    @abstractmethod
    def add_movie(self, movie: Movie):
        pass

    @abstractmethod
    def get_movie(self, movie_id):
        pass

    @abstractmethod
    def list_movies(self, page: int, filter_tags=None) -> dict:
        pass
