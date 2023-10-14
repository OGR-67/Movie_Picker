from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug import Response
from adapters.authentication_service_impl import AuthenticationServiceImpl
from adapters.db_connection import get_thread_db
from adapters.user_repository_impl import UserRepositoryImpl
from domain.services.user_service import UserService
from routes.middlewares.authentication_middlewares import check_authentication
from routes.forms.auth_forms import LoginOrRegistrationForm


authentication_bp = Blueprint('auth', __name__)


@authentication_bp.route('/register')
def register_page() -> str:
    try:
        form = LoginOrRegistrationForm()
        return render_template('register.html', form=form)
    except Exception:
        return render_template("500.html")


@authentication_bp.route("/register", methods=['POST'])
def register() -> Response | tuple[str, int]:
    form = LoginOrRegistrationForm(request.form)
    try:
        if form.validate_on_submit():
            username = request.form["username"]
            password = request.form["password"]

            user_repository = UserRepositoryImpl(get_thread_db())
            user_service = UserService(user_repository)
            user_service.register(username, password)

            return redirect(url_for('auth.login'))
        return render_template(
            'register.html', form=form, errors=form.errors
        ), 400
    except Exception as e:
        if str(e) == "Username already exists":
            return render_template(
                'register.html', form=form, error="Username already exists"
            ), 409
        return render_template('500.html'), 500


@authentication_bp.route('/login')
def login_page() -> str:
    try:
        form = LoginOrRegistrationForm()
        return render_template('login.html', form=form)
    except Exception:
        return render_template("500.html")


@authentication_bp.route('/login', methods=['POST'])
def login() -> Response | tuple[str, int]:
    form = LoginOrRegistrationForm(request.form)
    try:
        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']

            user_repository = UserRepositoryImpl(get_thread_db())
            user_service = UserService(user_repository)
            authentication_service = AuthenticationServiceImpl(user_service)

            authentication_service.login(username, password)

            return redirect(url_for('movies.home_movies'))
        return render_template(
            'login.html',
            form=form,
            errors=form.errors
        ), 401
    except Exception:
        return render_template(
            'login.html',
            form=form,
            error="Unable to connect with provided credentials"
        ), 401


@authentication_bp.route('/logout')
@check_authentication
def logout() -> Response | tuple[str, int]:
    try:
        user_repository = UserRepositoryImpl(get_thread_db())
        user_service = UserService(user_repository)
        authentication_service = AuthenticationServiceImpl(user_service)
        authentication_service.logout()

        return redirect(url_for('movies.home_movies'))
    except Exception:
        return "Logout failed", 401
