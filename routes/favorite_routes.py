from flask import Blueprint, Response, jsonify
from adapters.db_connection import get_thread_db
from adapters.favorite_repository_impl import FavoriteRepositoryImpl
from domain.services.favorite_service import FavoriteService
from routes.helpers.movie import get_movie_id
from routes.helpers.user import get_user_id
from routes.middlewares.authentication_middlewares import check_authentication


favorite_bp = Blueprint('favorites', __name__)


@favorite_bp.route('/add_movie', methods=['GET'])
@check_authentication
def add_movie() -> tuple[Response, int]:
    try:
        user_id = get_user_id()

        movie_id = get_movie_id()
        if movie_id == -1:
            return jsonify({"Invalid movie id"}), 400

        favorite_repository = FavoriteRepositoryImpl(get_thread_db())
        favorite_service = FavoriteService(favorite_repository)
        favorite_service.add_favorite(user_id, movie_id)

        return jsonify({"message": "Created"}), 200
    except (Exception) as e:
        return jsonify({"message": str(e)}), 500


@favorite_bp.route('/remove_movie', methods=['GET'])
@check_authentication
def remove_movie() -> tuple[Response, int]:
    try:
        user_id = get_user_id()

        movie_id = get_movie_id()
        if movie_id == -1:
            return jsonify({"Invalid movie id"}), 400

        favorite_repository = FavoriteRepositoryImpl(get_thread_db())
        favorite_service = FavoriteService(favorite_repository)
        favorite_service.remove_favorite(user_id, movie_id)

        return jsonify({"message": "Deleted"}), 200
    except (Exception) as e:
        return jsonify({"message": str(e)}), 500
