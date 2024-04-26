from fastapi import FastAPI

app = FastAPI()

@app.get("/heath-check", response_model=str)
async def health_check():
  return "App Age-Group is up and running"
