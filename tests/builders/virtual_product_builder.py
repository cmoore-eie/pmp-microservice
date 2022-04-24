import datetime

import requests

from models.virtual_product_model import VirtualProduct, VirtualProductFlavour, VirtualProductCategory, \
    VirtualProductContract, VirtualProductLine


class VirtualProductBuilder:
    def __init__(self):
        self.virtual_product = VirtualProduct()

    def build(self):
        self.virtual_product.product_code = 'dummy'
        self.virtual_product.name = 'dummy'
        self.virtual_product.effective_date = datetime.datetime.now()
        self.virtual_product.item_status = 'draft'
        # url = "http://127.0.0.1:5000/pmp/APAActionTypes"
        # response = requests.request("GET", url, headers={}, data='')
        # self.virtual_product.virtual_product_type = response.json()[0].get('id')
        return self.virtual_product

    def build_full(self) -> VirtualProduct:
        self.build()
        self.add_category()
        self.add_contract()
        self.add_flavour()
        self.add_line()
        return self.virtual_product

    def add_category(self):
        category = VirtualProductCategoryBuilder().build()
        category.name = 'Category Name 1'
        category.code = 'Category 1' # Add code conversion function that mimics what PMP has
        self.virtual_product.virtual_product_categories.append(category)

    def add_contract(self):
        contract = VirtualProductContractBuilder().build()
        self.virtual_product.virtual_product_contracts.append(contract)

    def add_flavour(self):
        flavour = VirtualProductFlavourBuilder().build()
        self.virtual_product.virtual_product_flavours.append(flavour)

    def add_line(self):
        line = VirtualProductLineBuilder().build()
        self.virtual_product.virtual_product_lines.append(line)


class VirtualProductCategoryBuilder:
    def __init__(self):
        self.category = None

    def build(self):
        self.category = VirtualProductCategory()
        return self.category


class VirtualProductContractBuilder:
    def __init__(self):
        self.contract = None

    def build(self):
        self.contract = VirtualProductContract()
        return self.contract


class VirtualProductFlavourBuilder:
    def __init__(self):
        self.flavour = None

    def build(self):
        self.flavour = VirtualProductFlavour()
        return self.flavour


class VirtualProductLineBuilder:
    def __init__(self):
        self.line = None

    def build(self):
        self.line = VirtualProductLine()
        return self.line
