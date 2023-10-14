import hashlib
from abc import ABC, abstractmethod
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository


class UserServiceInterface(ABC):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    @abstractmethod
    def register(self, username: str, password: str) -> User:
        pass

    @abstractmethod
    def login(self, username: str, password: str) -> User:
        pass

    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass

    @abstractmethod
    def delete_profile(self, user_id: int) -> None:
        pass


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, username: str, password: str) -> User:
        if len(password) < 8:
            raise Exception('Password too short')

        if len(username) < 4:
            raise Exception('Username too short')

        if ' ' in username:
            raise Exception('Username cannot contain spaces')

        for user in self.user_repository.get_users():
            if user.username == username:
                raise Exception('Username already exists')

        hashed_password = self.hash_password(password)
        return self.user_repository.add_user(username, hashed_password)

    def login(self, username: str, password: str) -> User:
        hashed_password = self.hash_password(password)

        user = self.user_repository.check_credentials(
            username,
            hashed_password
        )
        if user is None:
            raise Exception('username or password is incorrect')
        return user

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def delete_profile(self, user_id: int) -> None:
        self.user_repository.delete_user(user_id)
