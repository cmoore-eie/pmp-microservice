import json

import jsonpickle

from services.encoders import DateTimeEncoder


class Lookup:
    def __init__(self, in_id=None, in_type=None, in_code=None, in_name=None):
        self.id = in_id
        self.code = in_code
        self.name = in_name
        self.type = in_type

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, cls=DateTimeEncoder)

    def from_json(self, in_json):
        self.id = in_json['_id']
        self.code = in_json['code']
        self.name = in_json['name']
        self.type = in_json['type']
        return self
