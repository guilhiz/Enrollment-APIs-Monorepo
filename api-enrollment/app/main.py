from fastapi import FastAPI

app = FastAPI()

@app.get("/heath-check", response_model=str)
async def health_check():
  return "App Enrollment is up and running"