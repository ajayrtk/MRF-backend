from fastapi import FastAPI, HTTPException
from typing import List, Dict
from app.models import fetch_all_bookings, fetch_booking_by_id

app = FastAPI(title="Booking API", version="1.0")

@app.get("/bookings", response_model=List[Dict])
def get_bookings():
    try:
        bookings = fetch_all_bookings()
        return bookings
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

@app.get("/bookings/{exp_id}", response_model=Dict)
def get_booking(exp_id: int):
    try:
        booking = fetch_booking_by_id(exp_id)

        
        if booking is None:
            raise HTTPException(status_code=404, detail="Booking not found")
        return booking
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
