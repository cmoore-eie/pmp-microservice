import datetime

import requests

from models.condition_logic_model import ConditionLogic


class ConditionLogicBuilder:
    def __init__(self):
        self.condition_logic = ConditionLogic()

    def build(self):
        self.condition_logic.code = 'dummy'
        self.condition_logic.product_code = 'dummy'
        self.condition_logic.name = 'dummy'
        self.condition_logic.effective_date = datetime.datetime.now()
        self.condition_logic.item_status = 'draft'
        self.condition_logic.logic_code = 'dummy logic code'
        self.condition_logic.create_date = datetime.datetime.now()
        # url = "http://127.0.0.1:5000/pmp/APAActionTypes"
        # response = requests.request("GET", url, headers={}, data='')
        # self.virtual_product.virtual_product_type = response.json()[0].get('id')
        return self.condition_logic


