import unittest
import jsonpickle

from builders.condition_logic_builder import ConditionLogicBuilder
from models.condition_logic_model import ConditionLogic
from services import service
from services.http_status import HttpStatus
from models.virtual_product_model import VirtualProduct


class VirtualProductTest(unittest.TestCase):

    def setUp(self):
        condition_logic_builder = ConditionLogicBuilder()
        self.condition_logic_builder = condition_logic_builder
        self.condition_logic_model = condition_logic_builder.build()
        self.tester = service.app.test_client(self)
        self.delete_id = []

    def test_get_condition_logic(self):
        response = self.tester.get('/pmp/condition-logic')
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode))

    def test_create_condition_logic(self):
        condition_logic = self.condition_logic_builder.build()
        json_data = jsonpickle.encode(condition_logic, unpicklable=False)
        self.delete_id.append(condition_logic._id)
        response = self.tester.post('/pmp/condition-logic',
                                    data=json_data,
                                    content_type='application/json', )
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode))

        for item_id in self.delete_id:
            response = self.tester.get(f'/pmp/condition-logic/{item_id}')
            model = ConditionLogic().from_json(response.json)
            self.assertEqual(response.json['effective_date'], model.effective_date)
            self.assertEqual(response.json['_id'], model.item_identifier)

    def test_create_condition_logic_fail(self):
        condition_logic = self.condition_logic_builder.build()
        response = self.tester.post('/pmp/condition-logic')
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_client_error(statuscode))


if __name__ == '__main__':
    unittest.main()
