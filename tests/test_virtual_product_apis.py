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

    def test_get_virtual_products(self):
        response = self.tester.get('/pmp/virtualproducts')
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode))

    def test_create_virtual_products(self):
        virtual_product = self.virtual_model_builder.build_full()
        json_data = jsonpickle.encode(virtual_product, unpicklable=False)
        self.delete_id.append(virtual_product._id)
        response = self.tester.post('/pmp/virtualproduct',
                                    data=json_data,
                                    content_type='application/json', )
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode))

        for item_id in self.delete_id:
            response = self.tester.get(f'/pmp/virtualproduct/{item_id}')
            model = VirtualProduct().from_json(response.json)
            self.assertTrue(len(response.json['virtual_product_categories']) > 0)
            self.assertEqual(response.json['effective_date'], model.effective_date)
            self.assertEqual(response.json['_id'], model.item_identifier)

        #for item_id in self.delete_id:
           # response = self.tester.delete(f'/pmp/virtualproduct/{item_id}')

    def test_create_virtual_products_fail(self):
        virtual_product = self.virtual_model_builder.build_full()
        response = self.tester.post('/pmp/virtualproduct')
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_client_error(statuscode))


if __name__ == '__main__':
    unittest.main()
