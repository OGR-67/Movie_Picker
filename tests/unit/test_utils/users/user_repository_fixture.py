from domain.entities.user import User
from domain.repositories.user_repository import UserRepository


class UserRepositoryFixture(UserRepository):
    def __init__(self) -> None:
        self.users: list[User] = []

    def get_users(self) -> list[User]:
        return self.users

    def add_user(self, username: str, password: str) -> User:
        id = len(self.users) + 1
        user = User(id, username, password)
        self.users.append(user)
        return user

    def check_credentials(self, username: str, password: str) -> User | None:
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None
