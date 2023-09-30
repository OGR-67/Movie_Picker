import csv
from models.movie_model import Movie
from app import app, db
from flask import Flask

csv_file_path = "datas/mymoviedb.csv"


def feed() -> None:
    with app.app_context():
        with open(csv_file_path, newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)

            for line in csv_reader:
                movie = Movie(
                    title=line["Title"],
                    original_language=line["Original_Language"],
                    summary=line["Overview"],
                    release_date=line["Release_Date"],
                    poster_url=line["Poster_Url"],
                    genre=line["Genre"],
                    vote_average=float(
                        line["Vote_Average"]
                    ),
                )

                db.session.add(movie)

        db.session.commit()
    print("Datas import done.")


if __name__ == "__main__":
    feed()
