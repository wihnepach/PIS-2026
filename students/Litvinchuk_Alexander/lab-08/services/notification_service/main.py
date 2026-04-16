from event_bus.rabbitmq_config import EventBus


def handle_event(event):
    print(f"Notification received: {event}")


if __name__ == "__main__":
    bus = EventBus()
    bus.subscribe(handle_event)