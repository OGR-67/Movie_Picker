from flask import Flask
from models.movie_model import db
from flask_migrate import Migrate
from routes.movie_routes import movie_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies_db.db'
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(movie_bp)

if __name__ == "__main__":
    app.run()
