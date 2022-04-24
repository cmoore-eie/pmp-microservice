import json
import unittest

from services.pmptypes import PMPTypes
from tests.builders.virtual_product_builder import VirtualProductBuilder


class VirtualProductTest(unittest.TestCase):

    def setUp(self):
        self.virtual_model_builder = VirtualProductBuilder()
        self.virtual_model = self.virtual_model_builder.build()

    def test_virtual_product_model_init(self):
        self.assertTrue(self.virtual_model.base_type == PMPTypes.virtual_product.value)
        self.assertTrue(self.virtual_model.version_number == 1)
        self.assertIsNone(self.virtual_model.ancestor_item_identifier)
        self.assertIsNotNone(self.virtual_model.item_identifier)
        self.assertIsNotNone(self.virtual_model.name)
        self.assertIsNone(self.virtual_model.code)
        self.assertIsNotNone(self.virtual_model.item_status)
        self.assertTrue(len(self.virtual_model.virtual_product_categories) == 0)
        self.assertTrue(len(self.virtual_model.virtual_product_contracts) == 0)
        self.assertTrue(len(self.virtual_model.virtual_product_flavours) == 0)
        self.assertTrue(len(self.virtual_model.virtual_product_lines) == 0)
        self.assertIsNotNone(self.virtual_model.effective_date)
        self.assertIsNone(self.virtual_model.expiration_date)
        self.assertEqual(self.virtual_model.product_code, 'dummy')
        self.assertFalse(self.virtual_model.allow_affinity)
        self.assertFalse(self.virtual_model.allow_campaign)
        self.assertFalse(self.virtual_model.locked)

    def test_virtual_product_model_add_flavour(self):
        self.virtual_model_builder.add_flavour()
        self.assertTrue(len(self.virtual_model.virtual_product_flavours) == 1)
        self.assertIsNotNone(self.virtual_model.virtual_product_flavours[0].item_identifier)
        self.assertFalse(self.virtual_model.item_identifier == self.virtual_model.virtual_product_flavours[0]
                         .item_identifier)

    def test_virtual_product_model_json(self):
        virtual_product = self.virtual_model_builder.build_full()
        json_str = virtual_product.to_json()
        self.assertIsNotNone(json_str)
        json_dict = json.loads(json_str)
        self.assertIsNotNone(json_dict['virtual_product_categories'])
        self.assertIsNotNone(json_dict['virtual_product_contracts'])
        self.assertIsNotNone(json_dict['virtual_product_flavours'])
        self.assertIsNotNone(json_dict['virtual_product_lines'])


if __name__ == '__main__':
    unittest.main()
