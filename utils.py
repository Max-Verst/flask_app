import os


def get_sql_password():
    # Password can be passed directly or via a file (e.g. Docker secret)
    if "SQL_PASSWORD" in os.environ:
        return os.environ["SQL_PASSWORD"]
    if "SQL_PASSWORD_FILE" in os.environ:
        with open(os.environ["SQL_PASSWORD_FILE"]) as f:
            return f.read().strip()
    raise KeyError("Neither SQL_PASSWORD nor SQL_PASSWORD_FILE is set")


def get_postgres_database_uri():
    sql_user = os.environ["SQL_USER"]
    sql_password = get_sql_password()
    sql_host = os.environ["SQL_HOST"]
    sql_port = os.environ["SQL_PORT"]
    sql_database = os.environ["SQL_DATABASE"]
    return f"postgresql+psycopg://{sql_user}:{sql_password}@{sql_host}:{sql_port}/{sql_database}"