

class ImageToRecognitionMessage:
    def __init__(self, name, path):
        self.auth_token = name
        self.string_image = path
