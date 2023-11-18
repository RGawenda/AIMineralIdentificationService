import base64
from io import BytesIO

import tensorflow as tf
import config
from rabbitmq.ResultMessage import ResultMessage
from rabbitmq.ImageToRecognitionMessage import ImageToRecognitionMessage
import numpy as np
from PIL import Image
from scipy.special import softmax


class TensorflowModel:
    def __init__(self):
        self.tf_config = config.tensorflow_config
        self.class_names = self.tf_config.get('class_names')
        self.num_classes = self.tf_config.get('num_classes')
        model_path = self.tf_config.get('model_path')

        self.model = tf.keras.models.load_model(model_path)

    def predict(self, message_image: ImageToRecognitionMessage):
        result_image = ResultMessage(message_image.auth_token, "")

        decoded_bytes = base64.b64decode(message_image.string_image)

        image = Image.open(BytesIO(decoded_bytes))

        image = np.array(image)
        inn = self.tf_config.get('image_shape')
        image = tf.image.resize(image, inn)
        image = np.expand_dims(image, axis=0)

        predictions = self.model.predict(image)
        probabilities = softmax(predictions, axis=1)

        minerals_name = self.tf_config.get('class_names')
        predict_minerals = probabilities.tolist()
        predict_minerals = predict_minerals[0]
        result_map = {key: value for key, value in zip(minerals_name, predict_minerals)}

        result_image.predict_result = result_map

        return result_image
