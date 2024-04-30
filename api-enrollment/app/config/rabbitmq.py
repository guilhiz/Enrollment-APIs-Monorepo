import json
from typing import Dict

import pika
from decouple import config


class RabbitmqPublisher:
  def __init__(self) -> None:
    self.__host = config("RABBIT_HOST")
    self.__port = config("RABBIT_PORT")
    self.__username = config("RABBIT_USER")
    self.__password = config("RABBIT_PASSWORD")
    self.__exchange = "enrollment_exchange"
    self.__queue = "enrollment_queue"
    self.__routing_key = ""
    self.__channel = self.__create_channel()

  def __create_channel(self):
    connection_parameters = pika.ConnectionParameters(
        host=self.__host,
        port=self.__port,
        credentials=pika.PlainCredentials(
            username=self.__username,
            password=self.__password
        )
    )
    channel = pika.BlockingConnection(connection_parameters).channel()
    channel.exchange_declare(exchange=self.__exchange, exchange_type="direct",  durable=True)
    channel.queue_declare(queue=self.__queue, durable=True)
    channel.queue_bind(queue=self.__queue, exchange=self.__exchange, routing_key=self.__routing_key)
    return channel

  def send_message(self, body: Dict):
    self.__channel.basic_publish(
        exchange=self.__exchange,
        routing_key=self.__routing_key,
        body=json.dumps(body),
        properties=pika.BasicProperties(
            delivery_mode=2 # make message persistent
        )
    )
