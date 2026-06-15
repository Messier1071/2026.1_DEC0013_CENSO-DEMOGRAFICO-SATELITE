import sqlite3
from sqlite3 import Connection

def get_db_connection() -> Connection:
    # check_same_thread=False allows FastAPI and SQLite to work well togethre
    con = sqlite3.connect("density.db", check_same_thread=False)
    # row_factory to access columns by name (e.g., row['lat'])
    con.row_factory = sqlite3.Row
    return con

def setup_db():
    """Creates the database table if it doesn't exist."""
    con = get_db_connection()
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS search_locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT NOT NULL,
            lat REAL NOT NULL,
            lon REAL NOT NULL
        )
    ''')
    con.commit()
    con.close()