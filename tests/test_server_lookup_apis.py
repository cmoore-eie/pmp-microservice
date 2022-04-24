import unittest

import requests

from models.lookup_model import Lookup
from services import service
from services.http_status import HttpStatus
from services.pmptypes import PMPTypes

lookup_items = ['agreement-cancel-reasons',
                'agreement-status',
                'agreement-types',
                'apa-action-types',
                'apa--macro-inputs',
                'apa-macro-types',
                'attribute-value-types',
                'billing-producer-roles',
                'channels',
                'components',
                'condition-logic-opers',
                'condition-logic-types',
                'copy-clone-actions',
                'export-formats',
                'file-import-types',
                'item-status',
                'lead-follow',
                'negotiation-status',
                'schedule-contents',
                'schedule-functions',
                'schedule-identity-types',
                'scheme-Action-types',
                'scheme-Attachments',
                'scheme-calc-value-types',
                'scheme-card-filters',
                'scheme-condition-types',
                'scheme-cost-types',
                'scheme-create-methods',
                'scheme-Operator-types',
                'scheme-Source-types',
                'scheme-timeframes',
                'scheme-types',
                'scheme-validation-types',
                'scheme-value-types',
                'suspension-reasons',
                'system-setting-types',
                'virtual-flavour-actions',
                'virtual-product-types']


class LookupTest(unittest.TestCase):

    def setUp(self):
        self.tester = service.app.test_client(self)
        self.url = "http://127.0.0.1:5000"

    def tearDown(self) -> None:
        pass

    def test_by_codes(self):
        for item_type in lookup_items:
            url = f'{self.url}/pmp/{item_type}'
            response = requests.request("GET", url, headers={}, data='')
            statuscode = response.status_code
            self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')
            self.assertIsNotNone(response.json())
            for item in response.json():
                self.item_response(f'/pmp/{item_type}', item.get("id"))

    def item_response(self, item_url, item_id):
        url = f'{self.url}{item_url}/{item_id}'
        test_response = requests.request("GET", url, headers={}, data='')
        test_response_json = test_response.json()
        model = Lookup().from_json(test_response_json)
        self.assertTrue(model.type, PMPTypes.lookup_apa_action_type.value)
        self.assertEqual(model.id, test_response_json['_id'], f'while processing {url}')
        self.assertEqual(model.code, test_response_json['code'], f'while processing {url}')
        self.assertEqual(model.name, test_response_json['name'], f'while processing {url}')


if __name__ == '__main__':
    unittest.main()
