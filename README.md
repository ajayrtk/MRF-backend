# Booking API (FastAPI + SQLite)

This is a simple FastAPI-based REST API to fetch booking data from an SQLite database.

---

## Project Structure

MRF-BACKEND/
├── app/
│ ├── main.py # FastAPI application
│ ├── models.py # Database logic
│ └── database.py # SQLite connection
├── sqllite-db/
│ └── MRF_db.db # Your SQLite database
├── requirements.txt # Python dependencies
├── Dockerfile # Docker config
└── README.md # You're here


---

## Running Locally

### 1. Install Python dependencies

> Recommended: use a virtual environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


### 2. Run the FastAPI server 

```bash
uvicorn app.main:app --reload
```

* API: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Running with Docker

### 1. Build the Docker image

```bash
docker build -t booking-api .
```

### 2. Run the container

```bash
docker run -d -p 8000:8000 --name booking-api-container booking-api
```

* Now open: [http://localhost:8000](http://localhost:8000)

### 3. Show running containers

```bash
docker ps
```

### 4. Stop the container

```bash
docker stop booking-api-container
```

### 5. Remove the container

```bash
docker rm booking-api-container
```

---

## API Endpoints

| Method | Endpoint                 | Description                    |
| ------ | ------------------------ | ------------------------------ |
| GET    | `/`                      | Root endpoint (health check)   |
| GET    | `/bookings`              | Returns all booking records    |
| GET    | `/bookings/{session_id}` | Returns bookings by session ID |

---

## ⚠️ Notes

* Make sure the SQLite database file (`MRF_db.db`) exists under `sqllite-db/`.
* If using Docker, verify the path is correct in the `Dockerfile`.

---

## 📦 Dependencies

* FastAPI
* Uvicorn
* SQLite (built-in with Python)

Install them manually if needed:

```bash
pip install fastapi uvicorn
```
