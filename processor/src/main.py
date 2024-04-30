import json
import time

from src.config.mongodb import db_manager
from src.config.rabbitmq import RabbitmqConsumer


def callback(channel, method, properties, body):
    time.sleep(9)

    enrollment = json.loads(body)
    enroll_student(enrollment)


def enroll_student(enrollment):

    age_groups = list(db_manager.list_items())
    group = next(
        (group for group in age_groups
            if group["min_age"] <= enrollment["age"] <= group["max_age"]),
        None)

    enrollment["enrollment_status"] = "active" if group else "failed"
    enrollment["error_message"] = None if group else "No age group fits the provided age."

    db_manager.upsert_item(enrollment)

rabbitmq_consumer = RabbitmqConsumer(callback)
rabbitmq_consumer.start()
