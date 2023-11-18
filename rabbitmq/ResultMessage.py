

class ResultMessage:
    def __init__(self, name, result):
        self.user_name = name
        self.predict_result = result

    def to_dict(self):
        return {
            'authToken': self.user_name,
            'predict': self.predict_result
        }