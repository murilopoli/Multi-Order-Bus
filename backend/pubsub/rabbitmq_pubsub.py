import pika
from backend import config

class RabbitMQPubSub:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config.RABBITMQ_HOST, port=config.RABBITMQ_PORT)
        )
        self.channel = self.connection.channel()
        self.exchange = 'service_bus'
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='fanout')

    def publish(self, channel, message):
        self.channel.basic_publish(exchange=self.exchange, routing_key='', body=message)

    def subscribe(self, callback):
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.exchange, queue=queue_name)
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()
