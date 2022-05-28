from enum import Enum


class PMPBaseTypes(Enum):
    condition_logic = 'Condition Logic'
    scheme = 'Scheme'
    virtual_product = 'Virtual Product'
    virtual_product_category = 'Virtual Product Category'
    virtual_product_contract = 'Virtual Product Contract'
    virtual_product_flavour = 'Virtual Product Flavour'
    virtual_product_line = 'Virtual Product Line'
    negotiation = 'Negotiation'
    contract = 'Contract'

class PMPDesignDocument(Enum):
    virtual_product = 'virtual-product'
    lookup = 'lookup'

