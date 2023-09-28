from abc import ABC, abstractmethod
from domain.movie import Movie

class MovieRepository(ABC):
    @abstractmethod
    def add_movie(self, movie: Movie):
        pass
    
    @abstractmethod
    def get_movie(self, movie_id):
        pass
    
    @abstractmethod
    def list_movies(self):
        pass