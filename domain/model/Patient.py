import json


class Patient:
    def __init__(self, j):
        self.__dict__ = json.loads(j)