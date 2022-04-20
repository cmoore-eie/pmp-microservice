import datetime
from json import JSONEncoder


class DateTimeEncoder(JSONEncoder):
    def default(self, value):
        if isinstance(value, (datetime.date, datetime.datetime)):
            return value.isoformat()
        return value