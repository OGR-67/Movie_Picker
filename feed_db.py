import csv
from adapters.db_connection import get_thread_db

csv_file_path = "datas/mymoviedb.csv"
connection = get_thread_db()


def feed() -> None:
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
            connection.execute(insert_sql, movie_data)
        connection.commit()
    print("Datas import done.")


if __name__ == "__main__":
    feed()
