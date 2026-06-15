from fastapi import FastAPI
from app.Database import setup_db
from app.Controller import router

# Main API instance
app = FastAPI(
    title="Demographic Density API",
    description="MVC backend for demographic density estimation via satellite imagery and computer vision."
)

# Initialize the database
setup_db()

# Plug the controller routes into the main app
app.include_router(router)