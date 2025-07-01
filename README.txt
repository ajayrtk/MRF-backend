# Booking API - FastAPI + SQLite + Docker

This is a production-ready FastAPI backend that serves booking data from an existing SQLite database (`MRF_db.db`). The API includes endpoints to fetch all bookings or a single booking by `exp_id`. The service is containerized using Docker for easy deployment.

---

## 📁 Project Structure

.
├── app
│ ├── main.py # FastAPI routes
│ ├── models.py # DB query logic
│ ├── database.py # SQLite connection
├── sqllite-db
│ └── MRF_db.db # SQLite database (with booking_data table)
├── requirements.txt # Python dependencies
├── Dockerfile # Docker setup
└── README.txt # This file

yaml
Copy
Edit

---

## 🛠️ Requirements

- Docker
- (Optional for development) Python 3.8+

---

## ▶️ How to Run with Docker

1. **Build the Docker image:**

```bash
docker build -t booking-api .
Run the container:

bash
Copy
Edit
docker run -d -p 8000:8000 --name booking-api-container booking-api
Access the API:

All bookings:
http://localhost:8000/bookings

Single booking by exp_id:
http://localhost:8000/bookings/1

🗃️ Database Assumptions
Your SQLite database should exist at ./sqllite-db/MRF_db.db and contain a table named booking_data.

Example schema (assumed):
sql
Copy
Edit
CREATE TABLE booking_data (
    exp_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    booking_date TEXT,
    service TEXT,
    price REAL
);
Any NULL values in the DB will be returned as empty strings ("") in the JSON output.

🔧 Local Development (Optional)
You can also run the app locally:

bash
Copy
Edit
pip install -r requirements.txt
uvicorn app.main:app --reload
📦 Useful Docker Tips
To rebuild the image after changes:

bash
Copy
Edit
docker build --no-cache -t booking-api .
To stop and remove the container:

bash
Copy
Edit
docker stop booking-api-container && docker rm booking-api-container
To persist and edit the DB outside the container:

bash
Copy
Edit
docker run -d -p 8000:8000 \
  -v $(pwd)/sqllite-db:/app/sqllite-db \
  --name booking-api-container booking-api
✅ API Response Format
All responses are returned in valid JSON format.

Example:
json
Copy
Edit
{
  "exp_id": 1,
  "customer_name": "John Doe",
  "booking_date": "2025-07-01",
  "service": "Massage",
  "price": 150.00
}
License
This project is open-source and free to use.

