from flask import Blueprint, Response, jsonify, request, session
from adapters.db_connection import get_thread_db
from adapters.watchlist_repository_impl import WatchlistRepositoryImpl
from domain.services.watchlist_service import WatchlistService
from routes.middlewares.authentication_middlewares import check_authentication


watchlist_bp = Blueprint('watchlist', __name__)


@watchlist_bp.route('/add_movie', methods=['GET'])
@check_authentication
def add_movie() -> tuple[Response, int]:
    user = session["movie_picker_user"]
    user_id = user["id"]

    movie_id_str = request.args.get('movie_id')
    movie_id = int(
        movie_id_str
    ) if movie_id_str is not None and movie_id_str.isdigit() else -1
    if movie_id == -1:
        return jsonify({"Invalid movie id"}), 400
    watchlist_repository = WatchlistRepositoryImpl(get_thread_db())
    watchlist_service = WatchlistService(watchlist_repository)
    watchlist_service.add_to_watchlist(user_id, movie_id)
    return jsonify({"message": "Created"}), 200


@watchlist_bp.route('/remove_movie', methods=['GET'])
@check_authentication
def remove_movie() -> tuple[Response, int]:
    user = session["movie_picker_user"]
    user_id = user["id"]

    movie_id_str = request.args.get('movie_id')
    movie_id = int(
        movie_id_str
    ) if movie_id_str is not None and movie_id_str.isdigit() else -1

    if movie_id == -1:
        return jsonify({"Invalid movie id"}), 400
    watchlist_repository = WatchlistRepositoryImpl(get_thread_db())
    watchlist_service = WatchlistService(watchlist_repository)
    watchlist_service.remove_from_watchlist(user_id, movie_id)
    return jsonify({"message": "Deleted"}), 200
