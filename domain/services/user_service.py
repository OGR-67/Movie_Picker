from abc import ABC, abstractmethod
from domain.entities.user import User

from domain.repositories.user_repository import UserRepository


class UserServiceInterface(ABC):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    @abstractmethod
    def register(self, username: str, password: str) -> User:
        pass


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, username: str, password: str) -> User:
        if len(password) < 8:
            raise Exception('Password too short')

        if len(username) < 2:
            raise Exception('Username too short')

        if ' ' in username:
            raise Exception('Username cannot contain spaces')

        for user in self.user_repository.get_users():
            if user.username == username:
                raise Exception('Username already exists')

        hashed_password = str(hash(password))
        return self.user_repository.add_user(username, hashed_password)
