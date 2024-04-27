from fastapi import FastAPI
from app.routers.enrollment_routes import router
from app.config.db import enrollmentCollection

app = FastAPI()
app.include_router(router)


@app.get("/heath-check", response_model=str)
async def health_check():
    enrollments_count = enrollmentCollection.count_documents({})
    return f"App Enrollment is up and running. total enrollments: {enrollments_count}"
