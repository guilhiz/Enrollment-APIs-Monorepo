from app.models.enrollment import Enrollment
from app.config.db import ageCollection, enrollmentCollection

def enroll_student(enrollment: Enrollment):
    existing_student = enrollmentCollection.find_one({"cpf": enrollment.cpf})
    if existing_student:
        raise ValueError("A student with this CPF already exists.")

    age_groups = list(ageCollection.find())
    if any(group["min_age"] <= enrollment.age <= group["max_age"] for group in age_groups):
        enrollmentCollection.insert_one(dict(enrollment))
        return None
    else:
        raise ValueError("No age group fits the provided age.")
