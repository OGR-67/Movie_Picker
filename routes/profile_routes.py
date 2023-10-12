from flask import Blueprint, render_template
from routes.helpers.favorites import get_favorite_movies
from routes.helpers.user import get_user_id, get_username
from routes.helpers.watchlist import get_watchlist_movies
from routes.middlewares.authentication_middlewares import check_authentication


profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/')
@check_authentication
def profile() -> str:
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


@profile_bp.route('/delete', methods=['DELETE'])
@check_authentication
def delete_profile() -> tuple[str, int]:
    return 'Not implemented yet', 501
