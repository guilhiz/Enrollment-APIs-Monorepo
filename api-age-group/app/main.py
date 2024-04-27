from fastapi import FastAPI
from app.routers.ageGroup_routes import router

app = FastAPI()
app.include_router(router)


@app.get("/heath-check", response_model=str)
def health_check():
    return "App Age-Group is up and running"
