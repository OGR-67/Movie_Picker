import sqlite3
from domain.entities.favorite import Favorite
from domain.entities.movie import Movie
from domain.repositories.favorite_repository import FavoriteRepository


class FavoriteRepositoryImpl(FavoriteRepository):
    def __init__(self, db_connect: sqlite3.Connection) -> None:
        self.db_connect = db_connect

    def get_favorites(self, user_id: int) -> list[Favorite]:
        cursor = self.db_connect.cursor()
        cursor.execute(
            "SELECT * FROM favorites WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        return [Favorite(*row) for row in rows]

    def get_favorite_movies(self, user_id: int) -> list[Movie]:
        cursor = self.db_connect.cursor()
        cursor.execute(
            """
            SELECT movies.*
            FROM favorites
            JOIN movies ON movies.id = favorites.movie_id
            WHERE favorites.user_id = ?
            """,
            (user_id,)
        )
        rows = cursor.fetchall()
        return [Movie(*row) for row in rows]

    def add_favorite(self, user_id: int, movie_id: int) -> Favorite:
        cursor = self.db_connect.cursor()
        cursor.execute(
            """
            INSERT INTO favorites (user_id, movie_id)
            VALUES (?, ?)
            """,
            (user_id, movie_id)
        )
        self.db_connect.commit()
        favorite_id = cursor.lastrowid
        if favorite_id is None:
            raise Exception("Favorite not created")
        return Favorite(
            id=favorite_id,
            user_id=user_id,
            movie_id=movie_id
        )

    def remove_favorite(self, user_id: int, movie_id: int) -> None:
        cursor = self.db_connect.cursor()
        cursor.execute(
            """
            DELETE FROM favorites
            WHERE user_id = ? AND movie_id = ?
            """,
            (user_id, movie_id)
        )
        self.db_connect.commit()
