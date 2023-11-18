from rabbitmq.RabbitMqQueue import RabbitMqQueue

if __name__ == '__main__':
    rabbitmq = RabbitMqQueue()
    rabbitmq.recive_message()
