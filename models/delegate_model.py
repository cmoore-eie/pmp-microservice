import uuid


class ItemDelegate:
    def __init__(self):
        super(ItemDelegate, self).__init__()
        self.code = None
        self.locked = False


class ItemLinkDelegate:
    def __init__(self):
        super(ItemLinkDelegate, self).__init__()
        self.item_identifier = str(uuid.uuid4())
        self.ancestor_item_identifier = None
        self._id = self.item_identifier


class ItemStatusDelegate:
    def __init__(self):
        super(ItemStatusDelegate, self).__init__()
        self.item_status = None
        self.version_number: int = 1


class SchemeValueDelegate:
    def __init__(self):
        super(SchemeValueDelegate, self).__init__()
        self.string_value = None
        self.boolean_value = False
        self.date_value = None
        self.integer_value = 0
        self.decimal_value = 0.00
        self.long_value = None
        self.money_value = None
        self.scheme_calc_value_type = None


class SimpleEffDated:
    def __init__(self):
        super(SimpleEffDated, self).__init__()
        self.effective_date = None
        self.expiration_date = None


