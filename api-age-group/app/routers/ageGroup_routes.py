from fastapi import APIRouter, status, HTTPException, Response
from typing import List
from app.config.db import ageCollection
from app.models.age_group import AgeGroup, AgeGroupOut
from app.schemas.age_group import convert_age_groups
from bson import ObjectId

router = APIRouter(prefix="/age-groups", tags=["Age Groups"])

@router.get("/", response_model=List[AgeGroupOut], description="Get all age groups")
def get_age_groups():
    age_groups = ageCollection.find()
    converted_age_groups = convert_age_groups(age_groups)
    return converted_age_groups

@router.post("/", status_code=status.HTTP_201_CREATED, description="Create a new age group")
def add_age_group(age_group: AgeGroup):
    ageCollection.insert_one(dict(age_group))
    return Response(status_code=status.HTTP_201_CREATED)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, description="Delete an age group")
def delete_age_group(id: str):
    result = ageCollection.find_one_and_delete({"_id": ObjectId(id)})
    if result is None:
        raise HTTPException(status_code=404, detail="Age group not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
