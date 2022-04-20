import unittest

import test_lookup_apis
from tests import test_virtual_product_apis, test_virtual_product_models, test_lookup_model

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_lookup_apis))
suite.addTests(loader.loadTestsFromModule(test_virtual_product_apis))
suite.addTests(loader.loadTestsFromModule(test_virtual_product_models))
suite.addTests(loader.loadTestsFromModule(test_lookup_model))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)