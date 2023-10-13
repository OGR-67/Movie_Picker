from flask import Blueprint, Response, jsonify
from adapters.db_connection import get_thread_db
from adapters.watchlist_repository_impl import WatchlistRepositoryImpl
from domain.services.watchlist_service import WatchlistService
from routes.helpers.movie import get_movie_id
from routes.helpers.user import get_user_id
from routes.middlewares.authentication_middlewares import check_authentication


watchlist_bp = Blueprint('watchlist', __name__)


@watchlist_bp.route('/add_movie', methods=['GET'])
@check_authentication
def add_movie() -> tuple[Response, int]:
    try:
        user_id = get_user_id()

        movie_id = get_movie_id()
        if movie_id == -1:
            return jsonify({"Invalid movie id"}), 400

        watchlist_repository = WatchlistRepositoryImpl(get_thread_db())
        watchlist_service = WatchlistService(watchlist_repository)
        watchlist_service.add_to_watchlist(user_id, movie_id)

        return jsonify({"message": "Created"}), 200

    except (Exception) as e:
        return jsonify({"message": str(e)}), 500


@watchlist_bp.route('/remove_movie', methods=['GET'])
@check_authentication
def remove_movie() -> tuple[Response, int]:
    try:
        user_id = get_user_id()

        movie_id = get_movie_id()
        if movie_id == -1:
            return jsonify({"Invalid movie id"}), 400

        watchlist_repository = WatchlistRepositoryImpl(get_thread_db())
        watchlist_service = WatchlistService(watchlist_repository)
        watchlist_service.remove_from_watchlist(user_id, movie_id)

        return jsonify({"message": "Deleted"}), 200

    except (Exception) as e:
        return jsonify({"message": str(e)}), 500
