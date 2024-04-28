import pika

class RabbitmqConsumer:
  def __init__(self, callback) -> None:
    self.__host = "rabbitmq"  # Alterado de "localhost" para "rabbitmq"
    self.__port = 5672
    self.__username = "guest"
    self.__password = "guest"
    self.__queue = "enrollment_queue"
    self.__callback = callback
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

    channel = pika.BlockingConnection(
      connection_parameters
    ).channel()
    channel.queue_declare(queue=self.__queue, durable=True)

    channel.basic_consume(
      queue=self.__queue,
      on_message_callback=self.__callback,
      auto_ack=True
    )

    print("Waiting for messages...")

    channel.start_consuming()
    return channel

  def start(self):
    print(f"Listen RabbitMQ queue: {self.__queue}")
    self.__channel.start_consuming()

def callback(channel, method, properties, body):
  message = body.decode("utf-8")
  print(message)

rabbitmq_consumer = RabbitmqConsumer(callback)
rabbitmq_consumer.start()