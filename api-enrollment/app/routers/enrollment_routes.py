from fastapi import APIRouter, HTTPException, status, Response
from app.models.enrollment import Enrollment, EnrollmentOut
from app.schemas.enrollment import convert_enrollment
from app.services.enrollemnt_service import enroll_student
from app.config.db import enrollmentCollection
from app.config.rabbitmq import RabbitmqPublisher

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.get("/{cpf}", response_model=EnrollmentOut, description="Get enrollment status")
def get_enrollment_status(cpf: str):
    enrollment = enrollmentCollection.find_one({"cpf": cpf})
    if enrollment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")
    converted_enrollment = convert_enrollment(enrollment)
    return converted_enrollment

@router.post("/", status_code=status.HTTP_202_ACCEPTED, description="Enroll a new student")
def request_enrollment(enrollment: Enrollment):
    try:
        rabbitmq_publisher = RabbitmqPublisher()
        rabbitmq_publisher.send_message(dict(enrollment))
        # enroll_student(enrollment)
        return Response(status_code=status.HTTP_202_ACCEPTED)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
