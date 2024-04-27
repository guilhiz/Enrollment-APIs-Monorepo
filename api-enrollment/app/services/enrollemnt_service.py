from app.models.enrollment import Enrollment
from typing import List, Optional

# Mock data para os grupos etários
age_groups = [
    {"id": 1, "min_age": 0, "max_age": 2},
    {"id": 2, "min_age": 3, "max_age": 5},
    {"id": 3, "min_age": 15, "max_age": 30}
]

# Lista para armazenar as matrículas
enrollments: List[Enrollment] = []

def enroll_student(enrollment: Enrollment) -> Enrollment:
    # Verifica se a idade se encaixa em algum dos grupos etários
    if any(group['min_age'] <= enrollment.age <= group['max_age'] for group in age_groups):
        enrollments.append(enrollment)
        return enrollment
    else:
        raise ValueError("No age group fits the provided age.")

def check_enrollment(cpf: str) -> Optional[Enrollment]:
    for enrollment in enrollments:
        if enrollment.cpf == cpf:
            return enrollment
    return None