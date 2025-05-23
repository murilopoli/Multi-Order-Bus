import redis
from backend import config

class RedisPubSub:
    def __init__(self):
        self.r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)

    def publish(self, channel, message):
        self.r.publish(channel, message)

    def subscribe(self, channel):
        pubsub = self.r.pubsub()
        pubsub.subscribe(channel)
        return pubsub
