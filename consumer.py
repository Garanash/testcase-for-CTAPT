import argparse

from kafka import KafkaConsumer


def consume_messages(kafka_host, topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=kafka_host,
    )

    print("Starting to consume messages...")
    try:
        for message in consumer:
            print(f"Received message: {message.value.decode('utf-8')}")
    except Exception as e:
        print(f"Error consuming messages: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kafka Consumer")
    parser.add_argument('--kafka', type=str, required=True, help='Kafka host:port')
    parser.add_argument('--topic', type=str, required=True, help='Topic name')

    args = parser.parse_args()

    consume_messages(args.kafka, args.topic)
