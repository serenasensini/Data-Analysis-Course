import os
from typing import Any


def get_db_config() -> dict[str, Any]:
    return {
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3307")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "root"),
        "database": os.getenv("MYSQL_DATABASE", "lab03_movies"),
    }


def run_queries() -> None:
    import mysql.connector

    connection = mysql.connector.connect(**get_db_config())
    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT title, release_year FROM movies ORDER BY release_year ASC LIMIT 1")
        print("Film piu vecchio:", cursor.fetchone())

        cursor.execute("SELECT title, imdb_rating FROM movies ORDER BY imdb_rating DESC LIMIT 1")
        print("Film con rating migliore:", cursor.fetchone())

        # TODO (partecipanti): sostituire con query vera di conteggio film per anno.
        cursor.execute("SELECT 'TODO: completare query totali per anno' AS message")
        print("Totale film per anno:", cursor.fetchall())

        # TODO (partecipanti): aggiungere almeno una query filtro (es. per genere).
        cursor.close()
    finally:
        connection.close()


def main() -> None:
    if os.getenv("DRY_RUN", "1") == "1":
        print("DRY_RUN=1: scaffold pronto. Imposta DRY_RUN=0 per connetterti al DB.")
        return
    run_queries()


if __name__ == "__main__":
    main()

