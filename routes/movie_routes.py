from flask import Blueprint, render_template, request
from domain.movie import AVAILABLE_GENRE
from adapters.movie_repository_impl import MovieRepositoryImpl
from paths import DB_PATH

movie_bp = Blueprint('movies', __name__)


@movie_bp.route('/')
def home_movies():
    page = request.args.get("page")
    selected_tags = request.args.getlist('tags')

    if page is None or not page.isdigit():
        page = 1
    else:
        page = int(page)
    movies_repo = MovieRepositoryImpl(DB_PATH)
    query_result = movies_repo.list_movies(page)
    movies, total_pages = query_result["movies"], query_result["total_pages"]
    return render_template('home_movies.html', movies=movies, page=page, total_pages=total_pages, selected_tags=selected_tags, available_tags=AVAILABLE_GENRE)

# TODO: more movie routes here...
