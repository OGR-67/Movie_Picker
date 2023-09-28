import sqlite3
from domain.movie import Movie
from repositories.movie_repository import MovieRepository


class MovieRepositoryImpl(MovieRepository):
    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)

    def add_movie(self, movie: Movie):
        self.connect.execute("INSERT INTO movies (titre, annee, realisateur, bande_annonce_url) VALUES (?, ?, ?, ?)",
                             (movie.titre, movie.annee, movie.realisateur, movie.bande_annonce_url))
        self.connect.commit()

    def get_movie(self, movie_id):
        self.connect.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
        row = self.cursor.fetchone()
        if row:
            row["genre"] = self._string_list_to_array(row["genre"])
            return Movie(*row[1:])
        return None

    def list_movies(self, page):
        ITEMS_PER_PAGE = 20
        offset = (page - 1) * ITEMS_PER_PAGE

        count_cursor = self.connect.execute("SELECT COUNT(*) FROM movies")
        total_count = count_cursor.fetchone()[0]

        cursor = self.connect.execute(
            "SELECT * FROM movies LIMIT ? OFFSET ?", (ITEMS_PER_PAGE, offset))
        rows = cursor.fetchall()
        total_pages = (total_count + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

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

    def _string_list_to_array(self, string_list):
        items_array = [item.strip() for item in string_list.split(",")]
        return items_array
