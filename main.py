import argparse

from consumer import consume_messages
from producer import produce_message


def main():
    parser = argparse.ArgumentParser(description="Kafka Producer/Consumer")
    subparsers = parser.add_subparsers(dest="command", help="Subcommands")

    produce_parser = subparsers.add_parser('produce', help='Produce message')
    produce_parser.add_argument('--message', type=str, required=True, help='Message to send')
    produce_parser.add_argument('--topic', type=str, required=True, help='Topic name')
    produce_parser.add_argument('--kafka', type=str, required=True, help='Kafka host:port')

    consume_parser = subparsers.add_parser('consume', help='Consume messages')
    consume_parser.add_argument('--topic', type=str, required=True, help='Topic name')
    consume_parser.add_argument('--kafka', type=str, required=True, help='Kafka host:port')

    args = parser.parse_args()

    if args.command == 'produce':
        produce_message(args.kafka, args.topic, args.message)
    elif args.command == 'consume':
        consume_messages(args.kafka, args.topic)


if __name__ == "__main__":
    main()
