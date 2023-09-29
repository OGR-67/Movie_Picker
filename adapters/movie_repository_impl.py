import sqlite3
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository


class MovieRepositoryImpl(MovieRepository):
    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.ITEMS_PER_PAGE = 20

    def add_movie(self, movie: Movie):
        # Not implemented yet
        self.connect.execute("INSERT INTO movies (titre, annee, realisateur, bande_annonce_url) VALUES (?, ?, ?, ?)",
                             (movie.titre, movie.annee, movie.realisateur, movie.bande_annonce_url))
        # self.connect.commit()

    def get_movie(self, movie_id):
        # Not implemented yet
        # self.connect.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
        # row = self.cursor.fetchone()
        # if row:
        #     row["genre"] = self._string_list_to_array(row["genre"])
        #     return Movie(*row[1:])
        return None

    def list_movies(self, page: int, filter_tags=None, min_rating=0) -> dict:

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

        movies = []
        for row in rows:
            GENRE_INDEX = 6
            row = list(row)
            row[GENRE_INDEX] = self._string_list_to_array(row[GENRE_INDEX])
            movies.append(Movie(*row))
        return {
            "movies": movies,
            "total_pages": total_pages
        }

    def _string_list_to_array(self, string_list: str) -> list[str]:
        items_array = [item.strip() for item in string_list.split(",")]
        return items_array

    def _get_all_movies(self, min_rating, offset: int = 0):
        count_cursor = self.connect.execute(
            "SELECT COUNT(*) FROM movies WHERE vote_average > ?", (min_rating,))
        total_count = count_cursor.fetchone()[0]

        cursor = self.connect.execute(
            "SELECT * FROM movies WHERE vote_average > ? LIMIT ? OFFSET ?", (min_rating, self.ITEMS_PER_PAGE, offset))
        return total_count, cursor

    def _get_filtered_movies(self, filter_tags, offset, min_rating=0):
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
