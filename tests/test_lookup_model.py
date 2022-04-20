import json
import unittest

from builders.lookup_builder import LookupBuilder


class LookupModelTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lookup_model = LookupBuilder().build()

    def test_loopup_model_init(self):
        self.assertIsNotNone(self.lookup_model.code)
        self.assertIsNotNone(self.lookup_model.name)
        self.assertIsNotNone(self.lookup_model.type)

    def test_lookup_json(self):
        json_str = self.lookup_model.to_json()
        json_dict = json.loads(json_str)
        self.assertIsNotNone(json_dict)
        self.assertEqual(self.lookup_model.code, json_dict.get('code'))
        self.assertEqual(self.lookup_model.name, json_dict.get('name'))
        self.assertEqual(self.lookup_model.type, json_dict.get('type'))
