from flask import Blueprint, render_template, request, session
from adapters.authentication_service_impl import AuthenticationServiceImpl
from adapters.db_connection import get_thread_db
from adapters.user_repository_impl import UserRepositoryImpl
from domain.entities.movie import AVAILABLE_GENRE
from adapters.movie_repository_impl import MovieRepositoryImpl
from domain.services.movie_service import MovieService
from domain.services.user_service import UserService

movie_bp = Blueprint('movies', __name__)


@movie_bp.route('/')
def home_movies() -> str:
    user_repository = UserRepositoryImpl(get_thread_db())
    user_service = UserService(user_repository)
    authentication_service = AuthenticationServiceImpl(
        user_service
    )
    if authentication_service.is_logged_in():
        username = session["movie_picker_user"]
    else:
        username = None

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

    movies_repo = MovieRepositoryImpl(get_thread_db())
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
        min_rating=min_rating,
        username=username
    )


@movie_bp.route('/<int:movie_id>')
def movie_detail(movie_id: int) -> str:
    movies_repo = MovieRepositoryImpl(get_thread_db())
    movie = MovieService(movies_repo).get_movie_by_id(movie_id)
    return render_template(
        'movie_detail.html',
        movie=movie
    )

# TODO: more movie routes here...
