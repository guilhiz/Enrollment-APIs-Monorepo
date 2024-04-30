import time

import pika
from decouple import config


class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self.__host = config("RABBIT_HOST")
        self.__port = config("RABBIT_PORT")
        self.__username = config("RABBIT_USER")
        self.__password = config("RABBIT_PASSWORD")
        self.__queue = "enrollment_queue"
        self.__exchange = "enrollment_exchange"
        self.__routing_key = ""
        self.__callback = callback
        self.connection = None
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(username=self.__username, password=self.__password),
        )
        retries = 0
        while retries < 5:
            try:
                self.connection = pika.BlockingConnection(connection_parameters)
                break
            except pika.exceptions.AMQPConnectionError:
                retries += 1
                time.sleep(10)

        channel = self.connection.channel()
        channel.exchange_declare(exchange=self.__exchange, exchange_type="direct", durable=True)
        channel.queue_declare(queue=self.__queue, durable=True)
        channel.queue_bind(queue=self.__queue, exchange=self.__exchange, routing_key=self.__routing_key)

        channel.basic_consume(queue=self.__queue, on_message_callback=self.__callback, auto_ack=True)

        channel.start_consuming()
        return channel

    def start(self):
        self.__channel.start_consuming()
