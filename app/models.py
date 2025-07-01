from typing import List, Dict
from app.database import get_db_connection

def _replace_none_with_empty_str(data: Dict) -> Dict:
    return {k: ("" if v is None else v) for k, v in data.items()}

def fetch_all_bookings() -> List[Dict]:
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT * FROM booking_data")
        rows = cursor.fetchall()
        bookings = [_replace_none_with_empty_str(dict(row)) for row in rows]
        return bookings

def fetch_booking_by_id(exp_id: int) -> List[Dict]:
    with get_db_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM booking_data WHERE exp_id = ?", (exp_id,)
        )
        row = cursor.fetchone()
        if row:
            return _replace_none_with_empty_str(dict(row))
        return None