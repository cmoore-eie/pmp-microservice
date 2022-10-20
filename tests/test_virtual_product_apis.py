import unittest
import jsonpickle

from services import service
from services.http_status import HttpStatus
from tests.builders.virtual_product_builder import VirtualProductBuilder
from models.virtual_product_model import VirtualProduct


class VirtualProductTest(unittest.TestCase):

    def setUp(self):
        virtual_model_builder = VirtualProductBuilder()
        self.virtual_model_builder = virtual_model_builder
        self.virtual_model = virtual_model_builder.build()
        self.tester = service.app.test_client(self)
        self.delete_id = []

    def tearDown(self) -> None:
        url = f'/pmp/virtual-products/search'
        data = {'product_code': 'dummy'}
        data_string = jsonpickle.encode(data)
        response = self.tester.post(url, headers={'Content-Type': 'application/json'}, data=data_string)
        for item in response.json:
            item_id = item['_id']
            url = f'/pmp/virtual-products/{item_id}'
            # response = self.tester.delete(url)


    def test_create_virtual_products(self):
        virtual_product = self.virtual_model_builder.build_full()
        json_data = jsonpickle.encode(virtual_product, unpicklable=False)
        self.delete_id.append(virtual_product._id)
        response = self.tester.post('/pmp/virtual-products',
                                    data=json_data,
                                    content_type='application/json', )
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode))

        for item_id in self.delete_id:
            response = self.tester.get(f'/pmp/virtual-products/{item_id}')
            model = VirtualProduct().from_json(response.json)
            self.assertTrue(len(response.json['virtual_product_categories']) > 0)
            self.assertEqual(response.json['effective_date'], model.effective_date)
            self.assertEqual(response.json['_id'], model.item_identifier)

        # for item_id in self.delete_id:
        # response = self.tester.delete(f'/pmp/virtualproduct/{item_id}')

    def test_create_virtual_products_fail(self):
        response = self.tester.post('/pmp/virtual-products')
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_client_error(statuscode))

    def test_search_all(self):
        virtual_product = self.virtual_model_builder.build_full()
        json_data = jsonpickle.encode(virtual_product, unpicklable=False)
        response = self.tester.post('/pmp/virtual-products',
                                    data=json_data,
                                    content_type='application/json', )
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode))
        data = {"base_type": "Virtual Product"}
        json_data = jsonpickle.encode(data)
        response = self.tester.post('/pmp/virtual-products/search',
                                    data=json_data,
                                    content_type='application/json', )
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode))
        self.assertTrue(len(response.json) > 0)

    def test_find_by_effective_date(self):
        url = f'/pmp/virtual-products/search-effective'
        data = {'effective_date': '2000-01-01'}
        data_string = jsonpickle.encode(data)
        # response = self.tester.post(url, headers={'Content-Type': 'application/json'}, data=data_string)
        # statuscode = response.status_code
        # self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')


if __name__ == '__main__':
    unittest.main()
