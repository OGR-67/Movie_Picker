from models.movie_model import Movie
from domain.repositories.movie_repository import MovieRepository


class MovieService:
    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    def get_movie_by_id(self, movie_id) -> Movie:
        return self.movie_repository.get_movie(movie_id)

    def get_movies(self, page: int, filter_tags=None, min_rating=0) -> dict:
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
