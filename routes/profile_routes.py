from flask import Blueprint, Response, jsonify, render_template
from adapters.authentication_service_impl import AuthenticationServiceImpl
from adapters.db_connection import get_thread_db
from adapters.user_repository_impl import UserRepositoryImpl
from domain.services.user_service import UserService
from routes.helpers.favorites import get_favorite_movies
from routes.helpers.user import get_user_id, get_username
from routes.helpers.watchlist import get_watchlist_movies
from routes.middlewares.authentication_middlewares import check_authentication


profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/')
@check_authentication
def profile() -> str:
    try:
        username = get_username()
        user_id = get_user_id()

        favorite_movies = get_favorite_movies(user_id)
        watchlist_movies = get_watchlist_movies(user_id)

        return render_template(
            'profile.html',
            user_id=user_id,
            username=username,
            favorite_movies=favorite_movies,
            watchlist_movies=watchlist_movies
        )
    except Exception:
        return render_template("500.html")


@profile_bp.route('/delete')
@check_authentication
def delete_profile() -> tuple[Response, int]:
    try:
        user_id = get_user_id()

        user_repository = UserRepositoryImpl(get_thread_db())
        user_service = UserService(user_repository)

        authentication_service = AuthenticationServiceImpl(user_service)
        authentication_service.logout()

        user_service.delete_profile(user_id)

        return jsonify("Profile deleted successfully"), 200

    except (Exception) as e:
        return jsonify(str(e)), 500
