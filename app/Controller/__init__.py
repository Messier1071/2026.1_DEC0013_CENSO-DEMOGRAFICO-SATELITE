from fastapi import APIRouter
from app.Database import get_db_connection
from app.Model import LocationCreate

# The router manages the CRUD endpoints
router = APIRouter()

@router.post("/locations", status_code=201)
def create_location(location: LocationCreate):
    """Receives coordinates from the frontend and saves them to SQLite."""
    con = get_db_connection()
    cur = con.cursor()
    
    # Safe insertion against SQL Injection using "?" tuple
    cur.execute(
        "INSERT INTO search_locations (slug, lat, lon) VALUES (?, ?, ?)",
        (location.slug, location.lat, location.lon)
    )
    con.commit()
    new_id = cur.lastrowid
    con.close()
    
    return {"message": "Location successfully registered!", "id": new_id}

@router.get("/locations")
def list_locations():
    """Returns the entire search history saved in the database."""
    con = get_db_connection()
    cur = con.cursor()
    
    locations = cur.execute("SELECT * FROM search_locations").fetchall()
    con.close()
    
    # Converts database rows to dictionaries for FastAPI to parse into JSON
    return [dict(loc) for loc in locations]