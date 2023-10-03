from abc import ABC, abstractmethod
from domain.entities.user import User


class AuthenticationService(ABC):
    @abstractmethod
    def login(self, username: str, password: str) -> User:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

    @abstractmethod
    def is_logged_in(self) -> bool:
        pass
