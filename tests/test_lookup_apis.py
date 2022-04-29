import uuid
import time
import unittest

import jsonpickle

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
            # for item in response.json:
            #     self.item_response(f'{item_type.value}', item.get('key'))
            item_codes = list()
            for item in response.json:
                item_codes.append(item.get('code'))
            self.item_response_by_codes(f'{item_type.value}', ','.join(item_codes))
            end_time = time.time()
            print(f'Processed - {item_type.value} - {end_time - start_time}')

    def test_lookup_items(self):
        url = f'/pmp/lookup-types'
        response = self.tester.get(url)
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')
        self.assertIsNotNone(response.json, f'while processing {url}')
        data = response.json
        '''
        there is an additional 1 added to take into account the Test items that should be ignored'
        self.assertEqual(len(PMPLookupCodes) + 1, len(data), f'while processing {url}')
        '''
    def test_add_item(self):
        data = {
            'code': 'Test Code',
            'name': 'Test Name',
            'type': 'Test'}
        data_string = jsonpickle.encode(data)
        url = f'/pmp/lookup-items'
        response = self.tester.post(url, headers={'Content-Type': 'application/json'}, data=data_string)
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')

    def test_lookup_items_by_type(self):
        url = f'/pmp/lookup-types'
        response = self.tester.get(url)
        data = response.json
        for lookup_item in data:
            item = lookup_item.get('key')
            url = f'/pmp/lookup-items/type/{item}'
            response = self.tester.get(url)
            statuscode = response.status_code
            self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')
            self.assertIsNotNone(response.json, f'while processing {url}')

    def test_delete_valid_document(self):
        item_uuid = str(uuid.uuid4())
        print(f'Creating document : {item_uuid}')
        data = {
            '_id': item_uuid,
            'code': 'Test Code',
            'name': 'Test Name',
            'type': 'Test'}
        data_string = jsonpickle.encode(data)
        url = f'/pmp/lookup-items'
        response = self.tester.post(url, headers={'Content-Type': 'application/json'}, data=data_string)
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')
        print(f'Deleting document : {item_uuid}')
        url = f'/pmp/lookup-items/id/{item_uuid}'
        response = self.tester.delete(url)
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')
        print(f'Checking document : {item_uuid}')
        url = f'/pmp/lookup-items/id/{item_uuid}'
        response = self.tester.get(url)
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_client_error(statuscode), f'while processing {url}')


    def test_delete_invalid_document(self):
        url = f'/pmp/lookup-items/invalid_id'
        response = self.tester.delete(url)
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_client_error(statuscode), f'while processing {url}')

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
        url = f'/pmp/{item_url}/codes/{item_codes}'
        test_response = self.tester.get(url)
        self.assertEqual(len(item_codes.split(',')), len(test_response.json), f'while processing {url}')
        for item in test_response.json:
            self.assertIsNotNone(item.get('_id'), f'while processing {url}')
            self.assertIsNotNone(item.get('code'), f'while processing {url}')
            self.assertIsNotNone(item.get('name'), f'while processing {url}')
            model = Lookup().from_json(item)
            self.assertEqual(model.id, item.get('_id'), f'while processing {url}')
            self.assertEqual(model.code, item.get('code'), f'while processing {url}')
            self.assertEqual(model.name, item.get('name'), f'while processing {url}')


if __name__ == '__main__':
    unittest.main()
