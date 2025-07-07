from fastapi import FastAPI, HTTPException
from typing import List, Dict
from app.models import fetch_all_bookings, fetch_booking_by_session_id

app = FastAPI(title="Booking API", version="1.0")

@app.get("/", tags=["Root"])
def root():
    """
    Root endpoint to verify API is running.
    """
    return {"message": "Welcome to the Booking API"}

@app.get("/bookings", response_model=List[Dict], tags=["Bookings"])
def get_bookings():
    """
    Get all booking records from the database.
    """
    try:
        bookings = fetch_all_bookings()
        return bookings
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/bookings/{session_id}", response_model=List[Dict], tags=["Bookings"])
def get_booking_by_session_id(session_id: int):
    """
    Get booking(s) for a specific session ID.
    """
    try:
        bookings = fetch_booking_by_session_id(session_id)
        if not bookings:
            raise HTTPException(status_code=404, detail="No bookings found for the given session ID")
        return bookings
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify API is running.
    """
    return {"status": "ok", "message": "API is running smoothly"}   