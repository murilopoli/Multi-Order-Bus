from kafka import KafkaProducer, KafkaConsumer
from backend import config

class KafkaPubSub:
    def __init__(self):
        self.bootstrap_servers = f"{config.KAFKA_HOST}:{config.KAFKA_PORT}"

    def publish(self, topic, message):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
        producer.send(topic, message.encode('utf-8'))
        producer.flush()
        producer.close()

    def subscribe(self, topic):
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='service-bus-group'
        )
        return consumer
