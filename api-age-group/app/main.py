from fastapi import FastAPI

from app.config.mongodb import db_manager
from app.routers.ageGroup_routes import router

app = FastAPI()
app.include_router(router)


@app.get("/heath-check", response_model=str)
def health_check():
    age_groups_count = db_manager.count_items()
    return f"App Age-Group is up and running. Total age groups: {age_groups_count}"
