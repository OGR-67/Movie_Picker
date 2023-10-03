import csv
import os
import sqlite3
from sqlite3 import Connection
from flask import Flask
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session  # type: ignore
from sqlalchemy import create_engine
from paths import ROOT_DIR


def create_test_app() -> tuple[Connection, Flask]:
    memory_conn = sqlite3.connect(':memory:')
    create_engine('sqlite://', creator=lambda: memory_conn)

    app = Flask("test_app")

    app.config['TESTING'] = True
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)
    app.secret_key = "test_secret_key"

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'creator': lambda: memory_conn
    }

    db: SQLAlchemy = SQLAlchemy()
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        upgrade(directory=os.path.join(ROOT_DIR, "migrations"))

        csv_file_path = os.path.join(ROOT_DIR, "datas/mymoviedb_test.csv")
        with open(csv_file_path, newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            insert_sql = """
            INSERT INTO movies (
                title,
                original_language,
                summary,
                release_date,
                poster_url,
                genre,
                vote_average
                )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            for line in csv_reader:
                movie_data = (
                    line["Title"],
                    line["Original_Language"],
                    line["Overview"],
                    line["Release_Date"],
                    line["Poster_Url"],
                    line["Genre"],
                    float(line["Vote_Average"])
                )
                memory_conn.execute(insert_sql, movie_data)
            memory_conn.commit()

    return memory_conn, app


def rollback_and_close_db_connection(db_conn: sqlite3.Connection) -> None:
    db_conn.rollback()
    db_conn.close()
