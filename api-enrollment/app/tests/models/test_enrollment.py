import pytest
from pydantic import ValidationError
from app.models.enrollment import Enrollment

def test_enrollment_model():
  enrollment = Enrollment(name="John Doe", cpf="12345678901", age=30, enrollment_status="active" )
  assert enrollment.dict() == {"name": "John Doe", "cpf": "12345678901", "age": 30, "enrollment_status": "active"}

def test_enrollment_invalid_name():
  with pytest.raises(ValidationError):
    Enrollment(name="Jo", cpf="12345678901", age=30, enrollment_status="active" )

def test_enrollment_invalid_cpf():
  with pytest.raises(ValidationError):
    Enrollment(name="John Doe", cpf="123456789", age=30, enrollment_status="active")

  with pytest.raises(ValidationError):
    Enrollment(name="John Doe", cpf="123.456.789-012", age=30, enrollment_status="active")

def test_enrollment_invalid_age():
  with pytest.raises(ValidationError):
    Enrollment(name="John Doe", cpf="12345678901", age=0, enrollment_status="active" )