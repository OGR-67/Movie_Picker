import sqlite3
from typing import Any
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository


class MovieRepositoryImpl(MovieRepository):
    def __init__(self, db_file: str):
        self.connect = sqlite3.connect(db_file)
        self.ITEMS_PER_PAGE = 20

    def add_movie(self, movie: Movie) -> Movie:
        # Not implemented yet
        self.connect.execute("INSERT INTO movies (title, original_language, summary, release_date, poster_url, genre, vote_average) VALUES (?, ?, ?, ?, ?, ?, ?)",
                             (movie.title, movie.original_language, movie.summary, movie.release_date, movie.poster_url, ", ".join(movie.genre), movie.vote_average))
        # self.connect.commit()
        return movie

    def get_movie(self, movie_id: int) -> Movie | None:
        cursor = self.connect.execute(
            "SELECT * FROM movies WHERE id=?", (movie_id,))
        row = cursor.fetchone()
        GENRE_INDEX = 6
        if row:
            row = list(row)
            row[GENRE_INDEX] = self._string_list_to_array(row[GENRE_INDEX])
            return Movie(*row)
        return None

    def list_movies(
        self,
        page: int,
        filter_tags: list[str] | None = None,
        min_rating: float = 0.0
    ) -> dict[str, Any]:

        offset = (page - 1) * self.ITEMS_PER_PAGE

        if filter_tags is None:
            total_count, cursor = self._get_all_movies(min_rating, offset)
        else:
            total_count, cursor = self._get_filtered_movies(
                filter_tags,
                offset,
                min_rating
            )

        rows = cursor.fetchall()
        total_pages = (total_count + self.ITEMS_PER_PAGE -
                       1) // self.ITEMS_PER_PAGE

        movies = self._convert_rows_to_movies(rows)
        return {
            "movies": movies,
            "total_pages": total_pages
        }

    def _convert_rows_to_movies(self, rows: list[Any]) -> list[Movie]:
        movies = []
        for row in rows:
            GENRE_INDEX = 6
            row = list(row)
            row[GENRE_INDEX] = self._string_list_to_array(row[GENRE_INDEX])
            movies.append(Movie(*row))
        return movies

    def _string_list_to_array(self, string_list: str) -> list[str]:
        items_array = [item.strip() for item in string_list.split(",")]
        return items_array

    def _get_all_movies(self, min_rating: float, offset: int = 0) -> tuple[int, sqlite3.Cursor]:
        count_cursor = self.connect.execute(
            "SELECT COUNT(*) FROM movies WHERE vote_average > ?", (min_rating,))
        total_count = count_cursor.fetchone()[0]

        cursor = self.connect.execute(
            "SELECT * FROM movies WHERE vote_average > ? LIMIT ? OFFSET ?", (min_rating, self.ITEMS_PER_PAGE, offset))
        return total_count, cursor

    def _get_filtered_movies(
        self,
        filter_tags: list[str],
        offset: int,
        min_rating: float = 0
    ) -> tuple[int, sqlite3.Cursor]:
        params = ["%" + tag + "%" for tag in filter_tags]

        sql = "SELECT COUNT(*) FROM movies WHERE vote_average > ? AND (" + " OR ".join(
            ["genre LIKE ?" for _ in filter_tags]
        ) + ")"
        count_cursor = self.connect.execute(sql, (min_rating, *params))
        total_count = count_cursor.fetchone()[0]

        sql = "SELECT * FROM movies WHERE vote_average > ? AND (" + " OR ".join(
            ["genre LIKE ?" for _ in filter_tags]
        ) + ") LIMIT ? OFFSET ?"
        cursor = self.connect.execute(
            sql, (min_rating, *params, self.ITEMS_PER_PAGE, offset))

        return total_count, cursor
