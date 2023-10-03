from flask import Flask
from flask_session import Session  # type: ignore
from models.movie_model import db
from flask_migrate import Migrate
from routes.movie_routes import movie_bp
from routes.authentication_routes import authentication_bp

app = Flask(__name__)

# Cookies
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies_db.db'
db.init_app(app)
migrate = Migrate(app, db)

# Routes
app.register_blueprint(movie_bp)
app.register_blueprint(authentication_bp, url_prefix='/auth')

__all__ = ["app", "db"]

if __name__ == "__main__":
    app.secret_key = "secret_key"  # TODO: save in a file a more secure key
    app.run()
