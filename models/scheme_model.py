import jsonpickle

from models.delegate_model import ItemStatusDelegate, ItemDelegate, ItemLinkDelegate, SimpleEffDated, \
    SchemeValueDelegate
from services.pmptypes import PMPBaseTypes


class Scheme(ItemStatusDelegate, ItemDelegate, ItemLinkDelegate, SimpleEffDated):
    def __init__(self):
        super(Scheme, self).__init__()
        self.name = None
        self.product_code = None
        self.base_type = PMPBaseTypes.scheme
        self.details = []
        self.producers = []


class SchemeDetail(ItemLinkDelegate, SchemeValueDelegate):
    def __init__(self):
        super(SchemeDetail, self).__init__()
        self.comparator = None
        self.parent_code = None
        self.condition = None
        self.force_value = False
        self.time_duration = 0
        self.cost_discount = 0.00
        self.min_max = None
        self.segmentation = False
        self.scheme_source_type = None
        self.scheme_value_type = None
        self.scheme_action_type = None
        self.scheme_validation_type = None
        self.scheme_operator_type = None
        self.currency = None
        self.scheme_cost_type = None
        self.scheme_timeframe = None
        self.scheme_condition_type = None

    def to_json(self):
        return jsonpickle.encode(self)


class SchemeProducer(ItemLinkDelegate):
    def __init__(self):
        super(SchemeProducer, self).__init__()
        self.producer_code = None
        self.billing_producer_role = None
        self.commission_percentage = 0.00
        self.payer = False
        self.scheme_action_type = None
