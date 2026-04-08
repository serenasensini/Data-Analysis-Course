import os
from pathlib import Path

import mysql.connector
import pandas as pd


def get_db_config() -> dict:
    return {
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3307")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "root"),
        "database": os.getenv("MYSQL_DATABASE", "lab03_movies"),
    }


def load_csv_to_mysql(csv_path: Path) -> None:
    dataframe = pd.read_csv(csv_path)

    # TODO (partecipanti): aggiungere validazioni sulle colonne attese.
    records = list(
        dataframe[["title", "imdb_rating", "release_year", "genre", "duration_minutes"]]
        .itertuples(index=False, name=None)
    )

    connection = mysql.connector.connect(**get_db_config())
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM movies")
        cursor.executemany(
            """
            INSERT INTO movies (title, imdb_rating, release_year, genre, duration_minutes)
            VALUES (%s, %s, %s, %s, %s)
            """,
            records,
        )
        connection.commit()
        print(f"Import completato: {len(records)} righe caricate in tabella movies.")
    finally:
        connection.close()


def main() -> None:
    csv_path = Path(__file__).resolve().parent / "data" / "movies_dataset.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV non trovato: {csv_path}")
    load_csv_to_mysql(csv_path)


if __name__ == "__main__":
    main()

