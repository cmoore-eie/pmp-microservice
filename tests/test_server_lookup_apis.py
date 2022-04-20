import unittest

import requests

from models.lookup_model import Lookup
from services import service
from services.http_status import HttpStatus
from services.pmptypes import PMPTypes


class LookupTest(unittest.TestCase):

    def setUp(self):
        self.tester = service.app.test_client(self)
        self.url = "http://127.0.0.1:5000"

    def tearDown(self) -> None:
        pass

    def test_get_apa_action_type(self):
        response = self.list_response('/pmp/APAActionTypes')
        response_json = response.json()
        for item in response_json:
            self.item_response('/pmp/APAActionType', item.get("id"))

    def test_get_agreement_status(self):
        response = self.list_response('/pmp/AgreementStatuses')
        response_json = response.json()
        for item in response_json:
            self.item_response('/pmp/AgreementStatus', item.get("id"))

    def test_get_agreement_type(self):
        response = self.list_response('/pmp/AgreementTypes')
        response_json = response.json()
        for item in response_json:
            self.item_response('/pmp/AgreementType', item.get("id"))

    def test_get_item_status(self):
        response = self.list_response('/pmp/ItemStatuses')
        response_json = response.json()
        for item in response_json:
            self.item_response('/pmp/ItemStatus', item.get("id"))

    def test_get_virtual_product_type(self):
        response = self.list_response('/pmp/VirtualProductTypes')
        response_json = response.json()
        for item in response_json:
            self.item_response('/pmp/VirtualProductType', item.get("id"))

    def list_response(self, item_url):
        url = f'{self.url}{item_url}'
        response = requests.request("GET", url, headers={}, data='')
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode))
        self.assertIsNotNone(response.json())
        return response

    def item_response(self, item_url, item_id):
        url = f'{self.url}{item_url}/{item_id}'
        test_response = requests.request("GET", url, headers={}, data='')
        test_response_json = test_response.json()
        model = Lookup().from_json(test_response_json)
        self.assertTrue(model.type, PMPTypes.lookup_apa_action_type.value)
        self.assertEqual(model.id, test_response_json['_id'])
        self.assertEqual(model.code, test_response_json['code'])
        self.assertEqual(model.name, test_response_json['name'])


if __name__ == '__main__':
    unittest.main()
