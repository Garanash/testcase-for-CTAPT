# testcase-for-CTAPT

## Задание

Необходимо написать python-скрипт, который будет взаимодействовать с Apache Kafka следующим образом:
1. При исполнении команды

```bash 
python3 main.py produce --message 'Hello World!' --topic 'hello_topic' --kafka 'ip:9092'
```
Скрипт должен класть сообщение, указанное в параметре message в топик, указанный в параметре topic, в указанный инстанс Kafka.
2. При исполнении команды:

```bash
python3 main.py consume --topic 'hello_topic' --kafka 'ip:9092'
```
Скрипт должен подписаться на топик, указанный в параметре 'topic' и в бесконечном цикле выводить полученные сообщения.

3. Полученный скрипт нужно упаковать в docker образ. В качестве entrypoint указать скрипт.

4. Написать docker-compose файл, с помощью которого будут разворачиваться Apache Kafka


# Запуск

```bash
docker-compose up --build
```