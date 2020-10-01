class Patient:
    def __init__(self, json):
        self.age = json["age"]
        self.__dict__ = json
