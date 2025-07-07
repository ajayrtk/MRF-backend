import sqlite3
from contextlib import contextmanager
from fastapi import HTTPException

# Path to the SQLite database
DATABASE_PATH = "./sqllite-db/MRF_db.db"

@contextmanager
def get_db_connection():
    """
    Context manager to handle SQLite database connection with error handling.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row  # Enables accessing columns by name
        yield conn
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        conn.close()
