from fastapi import FastAPI
from app.routers.enrollment_routes import router

app = FastAPI()
app.include_router(router)
@app.get("/heath-check", response_model=str)
async def health_check():
  return "App Enrollment is up and running"
