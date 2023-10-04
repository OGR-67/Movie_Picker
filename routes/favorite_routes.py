from flask import Blueprint, Response, jsonify, request, session
from adapters.db_connection import get_thread_db
from adapters.favorite_repository_impl import FavoriteRepositoryImpl
from domain.services.favorite_service import FavoriteService
from routes.middlewares.authentication_middlewares import check_authentication


favorite_bp = Blueprint('favorites', __name__)


@favorite_bp.route('/add_movie', methods=['GET'])
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
    favorite_repository = FavoriteRepositoryImpl(get_thread_db())
    favorite_service = FavoriteService(favorite_repository)
    favorite_service.add_favorite(user_id, movie_id)
    return jsonify({"message": "Created"}), 200


@favorite_bp.route('/remove_movie', methods=['GET'])
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
    favorite_repository = FavoriteRepositoryImpl(get_thread_db())
    favorite_service = FavoriteService(favorite_repository)
    favorite_service.remove_favorite(user_id, movie_id)
    return jsonify({"message": "Deleted"}), 200
