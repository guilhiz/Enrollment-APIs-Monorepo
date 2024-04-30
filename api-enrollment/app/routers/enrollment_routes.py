from fastapi import APIRouter, HTTPException, Response, status

from app.config.mongodb import db_manager
from app.config.rabbitmq import RabbitmqPublisher
from app.models.enrollment import Enrollment, EnrollmentOut

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])




@router.get("/{cpf}", response_model=EnrollmentOut, description="Get enrollment status")
def get_enrollment_status(cpf: str):
    enrollment = db_manager.read_item({"cpf": cpf})

    if enrollment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Enrollment not found for CPF: " + cpf
        )

    return enrollment

@router.post("/", status_code=status.HTTP_202_ACCEPTED, description="Enroll a new student")
def request_enrollment(enrollment: Enrollment):
    try:
        rabbitmq_publisher = RabbitmqPublisher()
        message = dict(enrollment)
        rabbitmq_publisher.send_message(message)

        existing_enrollment = db_manager.read_item({"cpf": enrollment.cpf})
        if existing_enrollment:
            message_suffix = "being reprocessed to verify eligibility."
        else:
            message_suffix = "accepted. Your application is currently being processed."

        return f"Enrollment request {message_suffix}"

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
