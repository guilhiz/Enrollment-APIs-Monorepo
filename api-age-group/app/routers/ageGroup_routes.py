from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.config.auth.auth import verify_credentials
from app.config.mongodb import db_manager
from app.models.age_group import AgeGroup, AgeGroupOut

router = APIRouter(prefix="/age-groups", tags=["Age Groups"])


@router.get("/", response_model=List[AgeGroupOut], description="Get all age groups")
def get_age_groups(_: str = Depends(verify_credentials)):
    return db_manager.list_items()


@router.post("/", status_code=status.HTTP_201_CREATED, description="Create a new age group")
def add_age_group(age_group: AgeGroup, _: str = Depends(verify_credentials)):
    return db_manager.add_item(dict(age_group))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, description="Delete an age group")
def delete_age_group(id: str, _: str = Depends(verify_credentials)):
    result = db_manager.delete_item(id)
    if result is None:
        raise HTTPException(status_code=404, detail="Age group not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
