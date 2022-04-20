from models.lookup_model import Lookup


class LookupBuilder:
    def __init__(self):
        self.lookup = Lookup()

    def build(self) -> Lookup:
        self.lookup.code = 'sample1'
        self.lookup.name = 'Sample 1'
        self.lookup.type = 'Sample Lookup'
        return self.lookup
