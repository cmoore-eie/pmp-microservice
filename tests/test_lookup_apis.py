import time
import unittest

from models.lookup_model import Lookup
from services import service
from services.http_status import HttpStatus
from services.pmp_lookup import PMPLookupCodes


class LookupTest(unittest.TestCase):

    def setUp(self):
        self.tester = service.app.test_client(self)

    def tearDown(self) -> None:
        pass

    def test_by_codes(self):
        for item_type in PMPLookupCodes:
            start_time = time.time()
            url = f'/pmp/{item_type.value}'
            response = self.tester.get(url)
            statuscode = response.status_code
            self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')
            self.assertIsNotNone(response.json)
            for item in response.json:
                self.item_response(f'{item_type.value}', item.get('key'))
            for item in response.json:
                self.item_response_by_code(f'{item_type.value}', item.get('value'))
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

    def item_response_by_code(self, item_url, item_id):
        url = f'/pmp/{item_url}/codes/{item_id}'
        test_response = self.tester.get(url)
        self.assertIsNotNone(test_response.json['_id'], f'while processing {url}')
        self.assertIsNotNone(test_response.json['code'], f'while processing {url}')
        self.assertIsNotNone(test_response.json['name'], f'while processing {url}')
        model = Lookup().from_json(test_response.json)
        self.assertEqual(model.id, test_response.json['_id'], f'while processing {url}')
        self.assertEqual(model.code, test_response.json['code'], f'while processing {url}')
        self.assertEqual(model.name, test_response.json['name'], f'while processing {url}')


if __name__ == '__main__':
    unittest.main()
