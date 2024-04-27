from fastapi import APIRouter, HTTPException, status
from app.models.enrollment import Enrollment
from app.services.enrollemnt_service import enroll_student, check_enrollment

router = APIRouter(prefix='/enrollments', tags=['Enrollments'])

@router.post("/", response_model=Enrollment, status_code=status.HTTP_201_CREATED, description="Enroll a new student")
def request_enrollment(enrollment: Enrollment):
    try:
        return enroll_student(enrollment)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{cpf}", response_model=Enrollment, description="Get enrollment status")
def get_enrollment_status(cpf: str):
    enrollment = check_enrollment(cpf)
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment
