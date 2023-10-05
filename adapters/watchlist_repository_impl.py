import sqlite3
from domain.entities.watchlist_item import WatchlistItem
from domain.repositories.watchlist_repository import WatchlistRepository


class WatchlistRepositoryImpl(WatchlistRepository):
    def __init__(self, db_connect: sqlite3.Connection) -> None:
        self.db_connect = db_connect

    def get_watchlist(self, user_id: int) -> list[WatchlistItem]:
        cursor = self.db_connect.cursor()
        cursor.execute(
            "SELECT * FROM watchlist WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        return [WatchlistItem(*row) for row in rows]

    def add_item(self, user_id: int, movie_id: int) -> WatchlistItem:
        cursor = self.db_connect.cursor()
        cursor.execute(
            """
            INSERT INTO watchlist (user_id, movie_id)
            VALUES (?, ?)
            """,
            (user_id, movie_id)
        )
        self.db_connect.commit()
        favorite_id = cursor.lastrowid
        if favorite_id is None:
            raise Exception("Watchlist item not created")
        return WatchlistItem(
            id=favorite_id,
            user_id=user_id,
            movie_id=movie_id
        )

    def remove_item(self, user_id: int, movie_id: int) -> None:
        cursor = self.db_connect.cursor()
        cursor.execute(
            """
            DELETE FROM watchlist
            WHERE user_id = ? AND movie_id = ?
            """,
            (user_id, movie_id)
        )
        self.db_connect.commit()
