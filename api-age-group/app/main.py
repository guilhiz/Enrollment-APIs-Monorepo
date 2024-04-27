from fastapi import FastAPI
from app.routers.ageGroup_routes import router
from app.config.db import ageCollection

app = FastAPI()
app.include_router(router)

@app.get("/heath-check", response_model=str)
def health_check():
    age_groups_count = ageCollection.count_documents({})
    return f"App Age-Group is up and running. Total age groups: {age_groups_count}"
