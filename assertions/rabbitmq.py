from typing import List
from kombu import Connection, Consumer, Producer, Queue, Exchange

def assert_in(obj, objects):
    assert obj in objects

def assert_messages_received(connection_string, queue, expected_messages: List[bytes], timeout=120):
    with Connection(connection_string) as connection:
        with connection.channel() as channel:
            consumer = Consumer(channel, [Queue(queue)], callbacks=[
                lambda body, message : assert_in(body, expected_messages)
            ])

            consumer.consume()
            received_messages = 0
            while received_messages < len(expected_messages):
                received_messages +=1
                connection.drain_events(timeout=timeout)

def publish_messages(connection_string, exchange, messages: List[bytes]):
     with Connection(connection_string) as connection:
        with connection.channel() as channel:
            producer = Producer(channel, Exchange(exchange))
            for message in messages:
                producer.publish(message)