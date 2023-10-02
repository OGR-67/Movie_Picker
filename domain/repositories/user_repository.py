from abc import ABC, abstractmethod
from domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_users(self) -> list[User]:
        pass

    @abstractmethod
    def add_user(self, username: str, password: str) -> User:
        pass
