from flask import Blueprint, render_template, request
from domain.entities.movie import AVAILABLE_GENRE
from adapters.movie_repository_impl import MovieRepositoryImpl
from paths import DB_PATH
from domain.services.movie_service import MovieService

movie_bp = Blueprint('movies', __name__)


@movie_bp.route('/')
def home_movies() -> str:
    page_str = request.args.get("page")
    if page_str is None or not page_str.isdigit():
        page = 1
    else:
        page = int(page_str)

    selected_tags = request.args.getlist('tags') or None

    min_rating_str = request.args.get("min_rating")
    if min_rating_str is None or not min_rating_str.isdigit():
        min_rating = 0
    else:
        min_rating = int(min_rating_str)

    movies_repo = MovieRepositoryImpl(DB_PATH)
    query_result = MovieService(movies_repo).get_movies(
        page, selected_tags, min_rating)
    movies, total_pages = query_result["movies"], query_result["total_pages"]

    return render_template(
        'home_movies.html',
        movies=movies,
        page=page,
        total_pages=total_pages,
        selected_tags=selected_tags,
        available_tags=AVAILABLE_GENRE,
        min_rating=min_rating
    )

# TODO: more movie routes here...
