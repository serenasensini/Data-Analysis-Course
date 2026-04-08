import os
from typing import Any


def get_db_config() -> dict[str, Any]:
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "root"),
        "database": os.getenv("DB_NAME", "lab02db"),
    }


def get_connection(config: dict[str, Any]):
    """Create a MySQL connection.

    TODO (participants): add retries/backoff and better error handling.
    """
    import mysql.connector

    return mysql.connector.connect(**config)


def run_queries(connection) -> None:
    cursor = connection.cursor(dictionary=True)

    # Query 1: already implemented as a reference.
    cursor.execute("SELECT COUNT(*) AS total_employees FROM employees")
    print("Total employees:", cursor.fetchone())

    # Query 2: to be completed by participants.
    # TODO (participants): replace this placeholder query with:
    # SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department
    cursor.execute("SELECT 'TODO: complete department salary query' AS message")
    print("Department salary query:", cursor.fetchall())

    # Query 3: to be completed by participants.
    # TODO (participants): implement a query for oldest employee(s).

    cursor.close()


def main() -> None:
    if os.getenv("DRY_RUN", "1") == "1":
        print("DRY_RUN enabled: app scaffold is ready. Disable DRY_RUN to connect to MySQL.")
        return

    config = get_db_config()
    connection = get_connection(config)
    try:
        run_queries(connection)
    finally:
        connection.close()


if __name__ == "__main__":
    main()

