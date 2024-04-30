import pytest
from pydantic import ValidationError

from app.models.enrollment import Enrollment


def test_enrollment_model():
    enrollment = Enrollment(name="John Doe", cpf="12345678901", age=30)
    assert enrollment.dict() == {"name": "John Doe", "cpf": "12345678901", "age": 30}


def test_enrollment_with_too_short_name():
    with pytest.raises(ValidationError):
        Enrollment(name="Jo", cpf="12345678901", age=30)


def test_enrollment_with_too_long_name():
    with pytest.raises(ValidationError):
        Enrollment(name="J" * 101, cpf="12345678901", age=30)


def test_enrollment_with_invalid_cpf_length():
    with pytest.raises(ValidationError):
        Enrollment(name="John Doe", cpf="123456789", age=30)


    with pytest.raises(ValidationError):
        Enrollment(name="John Doe", cpf="123456789012", age=30)


def test_enrollment_with_non_numeric_cpf():
    with pytest.raises(ValidationError):
        Enrollment(name="John Doe", cpf="123R456B789", age=30)


def test_enrollment_with_negative_age():
    with pytest.raises(ValidationError):
        Enrollment(name="John Doe", cpf="12345678901", age=-1)


def test_enrollment_with_zero_age():
    with pytest.raises(ValidationError):
        Enrollment(name="John Doe", cpf="12345678901", age=0)
