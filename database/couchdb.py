import os

from cloudant import CouchDB
from cloudant.error import CloudantDatabaseException
from dotenv import dotenv_values
from requests.adapters import HTTPAdapter

from services.pmp_databases import PMPDatabases

httpAdapter = HTTPAdapter(pool_connections=10, pool_maxsize=100)


class CouchDBConnector:
    def __init__(self):
        self.client = None
        self.session = None
        self.lookup_database = None
        self.virtual_product_database = None
        self.scheme_database = None
        config = dotenv_values(os.environ.get('PMP_MICROSERVICE_CONFIG'))
        self.db_user = config.get('COUCHDB_USER')
        self.db_password = config.get('COUCHDB_PASSWORD')
        self.db_url = config.get('COUCHDB_URL')
        self.connect()

    def connect(self):
        self.client = CouchDB(self.db_user, self.db_password, url=self.db_url, connect=True, auto_renew=True,
                              adapter=httpAdapter)
        self.session = self.client.session()

        try:
            self.lookup_database = self.client.create_database(PMPDatabases.lookup.value)
        except CloudantDatabaseException:
            self.lookup_database = self.client[PMPDatabases.lookup.value]

        try:
            self.virtual_product_database = self.client.create_database(PMPDatabases.virtual_product.value)
        except CloudantDatabaseException:
            self.virtual_product_database = self.client[PMPDatabases.virtual_product.value]

        try:
            self.scheme_database = self.client.create_database(PMPDatabases.scheme.value)
        except CloudantDatabaseException:
            self.scheme_database = self.client[PMPDatabases.scheme.value]


db_client = CouchDBConnector()
