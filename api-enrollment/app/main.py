from fastapi import FastAPI

from app.config.mongodb import db_manager
from app.routers.enrollment_routes import router

app = FastAPI()
app.include_router(router)


@app.get("/heath-check", response_model=str)
async def health_check():
    enrollments_count =  db_manager.count_items()
    return f"App Enrollment is up and running. total enrollments: {enrollments_count}"
