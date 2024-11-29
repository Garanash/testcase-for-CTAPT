#!/bin/bash

# Запуск контейнеров
docker-compose up -d

# Ожидание запуска Kafka
sleep 5

# Создание топика
docker exec kafka /opt/bitnami/kafka/bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Проверка создания топика
docker exec kafka /opt/bitnami/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
