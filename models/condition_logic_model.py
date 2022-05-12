import datetime
import jsonpickle as jsonpickle
from models.delegate_model import ItemStatusDelegate, ItemDelegate, ItemLinkDelegate, SimpleEffDated
from services.pmptypes import PMPTypes


class ConditionLogic(ItemStatusDelegate, ItemDelegate, ItemLinkDelegate, SimpleEffDated):
    def __init__(self):
        super(ConditionLogic, self).__init__()
        self.name = None
        self.product_code = None
        self.effective_date = datetime.datetime.now()
        self.base_type = PMPTypes.condition_logic.value
        self.logic_code = None
        self.create_date = None
        self.update_time = None

    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)

    def from_json(self, in_json):
        self.id = in_json['_id']
        self.name = in_json['name']
        self.product_code = in_json['product_code']
        self.item_identifier = in_json['item_identifier']
        self.code = in_json['code']
        self.base_type = in_json['base_type']
        self.item_status = in_json['item_status']
        self.version_number = in_json['version_number']
        self.ancestor_item_identifier = in_json['ancestor_item_identifier']
        self.locked = in_json['locked']
        self.expiration_date = in_json['expiration_date']
        self.effective_date = in_json['effective_date']
        self.logic_code = in_json['logic_code']
        return self
