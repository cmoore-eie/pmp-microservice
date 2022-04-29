import unittest

from common.conversion_util import code_value, abbreviation_value


class LookupTest(unittest.TestCase):

    def test_code_value(self):
        result = code_value('This is a test')
        self.assertEqual(result, 'thisisatest')
        result = code_value(1)
        self.assertIsNone(result)

    def test_abbreviation_value(self):
        result = abbreviation_value('This is a test')
        self.assertEqual(result, 'THISISATEST')
        result = abbreviation_value(1)
        self.assertIsNone(result)
