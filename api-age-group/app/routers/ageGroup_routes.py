from fastapi import APIRouter, HTTPException
from typing import List
from app.models.age_group import AgeGroup

router = APIRouter(prefix="/age-groups", tags=["Age Groups"])

# Dados mockados para simular o armazenamento de grupos etários
age_groups = [AgeGroup(id=1, min_age=1, max_age=5), AgeGroup(id=2, min_age=20, max_age=30)]


@router.post("/", response_model=AgeGroup, status_code=201)
def add_age_group(age_group: AgeGroup):
    if any(group.id == age_group.id for group in age_groups):
        raise HTTPException(status_code=400, detail="Age group with this ID already exists")
    age_groups.append(age_group)
    return age_group


@router.delete("/{group_id}", status_code=204)
def delete_age_group(group_id: int):
    global age_groups
    age_groups = [group for group in age_groups if group.id != group_id]
    return {"message": "Age group deleted"}


@router.get("/", response_model=List[AgeGroup])
def get_age_groups():
    return age_groups
