import sqlite3
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self, connection: sqlite3.Connection):
        self.connect = connection

    def get_users(self) -> list[User]:
        cursor = self.connect.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return [User(*row) for row in rows]

    def add_user(self, username: str, password: str) -> User:
        try:
            self.connect.execute("BEGIN TRANSACTION")
            cursor = self.connect.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            self.connect.commit()
            if cursor.lastrowid is None:
                raise Exception('Could not register user')
            return User(cursor.lastrowid, username, password)
        except Exception as e:
            self.connect.rollback()
            raise e

    def check_credentials(self, username: str, password: str) -> User | None:
        cursor = self.connect.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        row = cursor.fetchone()
        if row is None:
            return None
        return User(*row)
