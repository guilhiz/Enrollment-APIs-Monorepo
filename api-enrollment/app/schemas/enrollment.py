def convert_enrollment(enrollment):
    return {
        "id": str(enrollment["_id"]),
        "name": enrollment["name"],
        "cpf": enrollment["cpf"],
        "age": enrollment["age"],
        "enrollment_status": enrollment["enrollment_status"],
    }


def convert_enrollments(enrollments):
    return [convert_enrollment(enrollment) for enrollment in enrollments]
