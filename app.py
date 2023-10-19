from flask import Flask, render_template
from flask_migrate import Migrate
from flask_session import Session  # type: ignore
from flask_sqlalchemy import SQLAlchemy
from routes.movie_routes import movie_bp
from routes.authentication_routes import authentication_bp
from routes.favorite_routes import favorite_bp
from routes.watchlist_routes import watchlist_bp
from routes.profile_routes import profile_bp
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

# Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies_db.db'
db: SQLAlchemy = SQLAlchemy()
db.init_app(app)
Migrate(app, db)


# Routes
app.register_blueprint(movie_bp)
app.register_blueprint(authentication_bp, url_prefix='/auth')
app.register_blueprint(favorite_bp, url_prefix='/favorites')
app.register_blueprint(watchlist_bp, url_prefix='/watchlist')
app.register_blueprint(profile_bp, url_prefix='/profile')


@app.errorhandler(404)
def page_not_found(e: HTTPException) -> tuple[str, int]:
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e: HTTPException) -> tuple[str, int]:
    return render_template('500.html'), 500


__all__ = ["app"]

if __name__ == "__main__":
    # NOTE: For production deployments, store the key in a secure file.
    app.secret_key = "secret_key"
    app.run()
