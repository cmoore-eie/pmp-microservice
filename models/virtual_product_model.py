import datetime
import jsonpickle as jsonpickle
from models.delegate_model import ItemStatusDelegate, ItemDelegate, ItemLinkDelegate, SimpleEffDated
from services.pmptypes import PMPBaseTypes


class VirtualProduct(ItemStatusDelegate, ItemDelegate, ItemLinkDelegate, SimpleEffDated):
    def __init__(self):
        super(VirtualProduct, self).__init__()
        effective_date = datetime.datetime
        self.allow_affinity = False
        self.allow_campaign = False
        self.name = None
        self.product_code = None
        self.effective_date = effective_date.now()
        self.base_type = PMPBaseTypes.virtual_product.value
        self.virtual_product_type = None
        self.virtual_product_categories: list[VirtualProductCategory] = list()
        self.virtual_product_contracts: list[VirtualProductContract] = list()
        self.virtual_product_flavours: list[VirtualProductFlavour] = list()
        self.virtual_product_lines: list[VirtualProductLine] = list()

    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)

    def from_json(self, in_json):
        self.id = in_json['_id']
        self.name = in_json['name']
        self.product_code = in_json['product_code']
        self.allow_campaign = in_json['allow_campaign']
        self.allow_affinity = in_json['allow_affinity']
        self.item_identifier = in_json['item_identifier']
        self.code = in_json['code']
        self.base_type = in_json['base_type']
        self.item_status = in_json['item_status']
        self.version_number = in_json['version_number']
        self.ancestor_item_identifier = in_json['ancestor_item_identifier']
        self.locked = in_json['locked']
        self.expiration_date = in_json['expiration_date']
        self.effective_date = in_json['effective_date']
        return self


class VirtualProductCategory(ItemLinkDelegate):
    def __init__(self):
        super(VirtualProductCategory, self).__init__()
        self.base_type = PMPBaseTypes.virtual_product_category.value
        self.name = None
        self.code = None
        self.priority = 0


class VirtualProductContract(ItemLinkDelegate):
    def __init__(self):
        super(VirtualProductContract, self).__init__()
        self.base_type = PMPBaseTypes.virtual_product_contract.value


class VirtualProductFlavour(ItemLinkDelegate, SimpleEffDated):
    def __init__(self):
        super(VirtualProductFlavour, self).__init__()
        self.default = None
        self.base_type = PMPBaseTypes.virtual_product_flavour.value


class VirtualProductLine(ItemLinkDelegate):
    def __init__(self):
        super(VirtualProductLine, self).__init__()
        self.base_type = PMPBaseTypes.virtual_product_line.value
