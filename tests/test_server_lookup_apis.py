import json
import time
import unittest

import requests

from models.lookup_model import Lookup
from services import service
from services.http_status import HttpStatus
from services.pmp_lookup import PMPLookupCodes


class LookupTest(unittest.TestCase):

    def setUp(self):
        self.tester = service.app.test_client(self)
        self.url = "http://127.0.0.1:5000"

    def tearDown(self) -> None:
        pass

    def test_by_codes(self):
        for item_type in PMPLookupCodes:
            start_time = time.time()
            url = f'{self.url}/pmp/{item_type.value}'
            response = requests.request("GET", url, headers={}, data='')
            statuscode = response.status_code
            self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')
            self.assertIsNotNone(response.json())
            # for item in response.json:
            #     self.item_response(f'{item_type.value}', item.get('key'))
            item_codes = list()
            for item in response.json():
                item_codes.append(item.get('code'))
            self.item_response_by_codes(f'{item_type.value}', ','.join(item_codes))
            end_time = time.time()
            print(f'Processed - {item_type.value} - {end_time - start_time}')

    def item_response(self, item_url, item_id):
        url = f'/pmp/{item_url}/{item_id}'
        test_response = self.tester.get(url)
        self.assertIsNotNone(test_response.json['_id'], f'while processing {url}')
        self.assertIsNotNone(test_response.json['code'], f'while processing {url}')
        self.assertIsNotNone(test_response.json['name'], f'while processing {url}')
        model = Lookup().from_json(test_response.json)
        self.assertEqual(model.id, test_response.json['_id'], f'while processing {url}')
        self.assertEqual(model.code, test_response.json['code'], f'while processing {url}')
        self.assertEqual(model.name, test_response.json['name'], f'while processing {url}')

    def item_response_by_codes(self, item_url, item_codes):
        url = f'{self.url}/pmp/{item_url}/codes/{item_codes}'
        test_response = requests.request("GET", url, headers={}, data='')
        self.assertEqual(len(item_codes.split(',')), len(test_response.json()), f'while processing {url}')
        for item in test_response.json():
            self.assertIsNotNone(item.get('_id'), f'while processing {url}')
            self.assertIsNotNone(item.get('code'), f'while processing {url}')
            self.assertIsNotNone(item.get('name'), f'while processing {url}')
            model = Lookup().from_json(item)
            self.assertEqual(model.id, item.get('_id'), f'while processing {url}')
            self.assertEqual(model.code, item.get('code'), f'while processing {url}')
            self.assertEqual(model.name, item.get('name'), f'while processing {url}')


if __name__ == '__main__':
    unittest.main()
