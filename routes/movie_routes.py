from flask import Blueprint, render_template, request
from domain.entities.movie import AVAILABLE_GENRE
from adapters.movie_repository_impl import MovieRepositoryImpl
from paths import DB_PATH
from domain.services.movie_service import MovieService

movie_bp = Blueprint('movies', __name__)


@movie_bp.route('/')
def home_movies():
    page = request.args.get("page")
    page = int(page) if page is not None and page.isdigit() else 1

    selected_tags = request.args.getlist('tags') or None

    movies_repo = MovieRepositoryImpl(DB_PATH)
    query_result = MovieService(movies_repo).get_movies(page, selected_tags)
    movies, total_pages = query_result["movies"], query_result["total_pages"]
    print(movies[1])

    return render_template(
        'home_movies.html',
        movies=movies,
        page=page,
        total_pages=total_pages,
        selected_tags=selected_tags,
        available_tags=AVAILABLE_GENRE
    )

# TODO: more movie routes here...
