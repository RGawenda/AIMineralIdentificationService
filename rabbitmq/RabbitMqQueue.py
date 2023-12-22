import pika
import json
import config
from model_ai.TensorflowModel import TensorflowModel
from rabbitmq.ImageToRecognitionMessage import ImageToRecognitionMessage


class RabbitMqQueue:
    def __init__(self):
        self.rabbit_config = config.rabbitmq_config
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbit_config.get('adress')))
        self.model = TensorflowModel()

    def recive_message(self):
        channel = self.connection.channel()
        channel.queue_declare(queue=self.rabbit_config.get('queue_input'), durable=True)

        def callback(ch, method, properties, body):
            self.proces_image(body)

        channel.basic_consume(queue=self.rabbit_config.get('queue_input'), on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

    def proces_image(self, body):
        json_input = json.loads(body)
        json_input = json.loads(json_input)

        image_to_proces = ImageToRecognitionMessage(json_input['classificationID'], json_input['imageBase64'])
        result = self.model.predict(image_to_proces)
        result_to_send = json.dumps(result.to_dict())
        result_to_send = json.dumps(result_to_send)

        self.send_message(result_to_send)

    def send_message(self, message):
        print(message)
        channel = self.connection.channel()
        channel.queue_declare(queue=self.rabbit_config.get('queue_output'), durable=True)

        channel.basic_publish(exchange='', routing_key=self.rabbit_config.get('queue_output'), body=message)
