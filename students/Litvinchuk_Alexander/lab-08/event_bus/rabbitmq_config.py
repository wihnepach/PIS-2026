import pika
import json


class EventBus:
    def __init__(self, host="localhost"):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host)
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange="events", exchange_type="fanout")

    def publish(self, event_type: str, data: dict):
        message = json.dumps({"event": event_type, "data": data})

        self.channel.basic_publish(
            exchange="events",
            routing_key="",
            body=message
        )

    def subscribe(self, callback):
        result = self.channel.queue_declare(queue="", exclusive=True)
        queue_name = result.method.queue

        self.channel.queue_bind(exchange="events", queue=queue_name)

        def wrapper(ch, method, properties, body):
            event = json.loads(body)
            callback(event)

        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=wrapper,
            auto_ack=True
        )

        print("Waiting for events...")
        self.channel.start_consuming()