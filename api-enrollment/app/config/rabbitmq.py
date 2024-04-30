import json
from typing import Dict

import pika


class RabbitmqPublisher:
  def __init__(self) -> None:
    self.__host = "rabbitmq"
    self.__port = 5672
    self.__username = "guest"
    self.__password = "guest"
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
