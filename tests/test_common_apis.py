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

    def test_pmp_base_types(self):
        url = f'/pmp/common/base_types'
        response = self.tester.get(url)
        statuscode = response.status_code
        self.assertTrue(HttpStatus.is_success(statuscode), f'while processing {url}')
        self.assertIsNotNone(response.json)

if __name__ == '__main__':
    unittest.main()
