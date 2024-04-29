from src.config.rabbitmq import RabbitmqConsumer
from src.config.db import ageCollection, enrollmentCollection
import json
import time


def callback(channel, method, properties, body):
    message = body.decode("utf-8")
    print(f"Received message: {message}")
    time.sleep(3)
    enrollment = json.loads(body)
    enroll_student(enrollment)


def enroll_student(enrollment):
    existing_student = enrollmentCollection.find_one({"cpf": enrollment["cpf"]})
    if existing_student:
        update_enrollment_with_error(enrollment, "A student with this CPF already exists.")
        return

    age_groups = list(ageCollection.find())
    if not any(group["min_age"] <= enrollment["age"] <= group["max_age"] for group in age_groups):
        update_enrollment_with_error(enrollment, "No age group fits the provided age.")
        return

    enrollment["enrollment_status"] = "active"
    enrollmentCollection.insert_one(enrollment)


def update_enrollment_with_error(enrollment, error_message):
    enrollment["enrollment_status"] = "failed"
    enrollment["error_message"] = error_message
    enrollmentCollection.insert_one(enrollment)


rabbitmq_consumer = RabbitmqConsumer(callback)
rabbitmq_consumer.start()
