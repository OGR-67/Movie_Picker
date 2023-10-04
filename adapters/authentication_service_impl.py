from domain.services.authentication_service import AuthenticationService
from flask import session
from domain.entities.user import User
from domain.services.user_service import UserServiceInterface


class AuthenticationServiceImpl (AuthenticationService):
    def __init__(self, user_service: UserServiceInterface) -> None:
        self.user_service = user_service

    def login(self, username: str, password: str) -> User:
        user = self.user_service.login(username, password)
        session["movie_picker_user"] = user.username
        return user

    def logout(self) -> None:
        session.pop("movie_picker_user", None)

    def is_logged_in(self) -> bool:
        return "movie_picker_user" in session
