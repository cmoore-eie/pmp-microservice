import unittest
import test_server_lookup_apis

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_server_lookup_apis))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)