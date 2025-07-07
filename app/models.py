from typing import List, Dict, Optional
from app.database import get_db_connection

def _replace_none_with_empty_str(data: Dict) -> Dict:
    """
    Replace None values in a dict with empty strings to ensure cleaner API responses.
    """
    return {k: ("" if v is None else v) for k, v in data.items()}

def fetch_all_bookings() -> List[Dict]:
    """
    Fetch all bookings from the database.
    """
    with get_db_connection() as conn:
        try:
            cursor = conn.execute("SELECT * FROM booking_data")
            rows = cursor.fetchall()
            return [_replace_none_with_empty_str(dict(row)) for row in rows]
        except Exception as e:
            raise Exception(f"Error fetching all bookings: {e}")

def fetch_booking_by_session_id(session_id: int) -> List[Dict]:
    """
    Fetch bookings from the database by session ID.
    """
    with get_db_connection() as conn:
        try:
            cursor = conn.execute("SELECT * FROM booking_data WHERE SessionId = ?", (session_id,))
            rows = cursor.fetchall()
            return [_replace_none_with_empty_str(dict(row)) for row in rows]
        except Exception as e:
            raise Exception(f"Error fetching booking for SessionId {session_id}: {e}")
