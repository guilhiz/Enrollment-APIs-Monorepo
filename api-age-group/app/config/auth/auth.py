from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pathlib import Path
import json
import base64

security = HTTPBasic()

def get_credentials():
    credentials_path = Path(__file__).parent / 'credentials.json'

    with credentials_path.open("r") as file:
        credentials = json.load(file)
    return credentials
def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_credentials = get_credentials()
    correct_username = correct_credentials["username"]
    correct_password = correct_credentials["password"]
    if credentials.username == correct_username and credentials.password == correct_password:
        return credentials.username
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

def get_basic_auth_header(username: str, password: str):
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return {"Authorization": f"Basic {encoded_credentials}"}