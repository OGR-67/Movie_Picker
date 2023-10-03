from typing import Any, Callable
from flask import redirect, url_for
from adapters.authentication_service_impl import AuthenticationServiceImpl
from adapters.db_connection import DB_CONNECT
from adapters.user_repository_impl import UserRepositoryImpl

from domain.services.user_service import UserService


def check_authentication(
    view_function: Callable[..., Any]
) -> Callable[..., Any]:
    def wrapped_view(*args: Any, **kwargs: Any) -> Any:
        user_repository = UserRepositoryImpl(DB_CONNECT)
        user_service = UserService(user_repository)
        authentication_service = AuthenticationServiceImpl(user_service)
        if not authentication_service.is_logged_in():
            return redirect(url_for("/login"))
        return view_function(*args, **kwargs)
    return wrapped_view
