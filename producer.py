import argparse
from kafka import KafkaProducer


def produce_message(kafka_host, topic, message):
    producer = KafkaProducer(bootstrap_servers=kafka_host)
    future = producer.send(topic, value=message)
    result = future.get(timeout=10)
    print(f"Message sent successfully: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kafka Producer")
    parser.add_argument('--kafka', type=str, required=True, help='Kafka host:port')
    parser.add_argument('--topic', type=str, required=True, help='Topic name')
    parser.add_argument('--message', type=str, required=True, help='Message to send')

    args = parser.parse_args()

    produce_message(args.kafka, args.topic, args.message)
