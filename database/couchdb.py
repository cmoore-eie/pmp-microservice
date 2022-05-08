import os

from cloudant import CouchDB
from cloudant.error import CloudantDatabaseException
from dotenv import dotenv_values
from requests.adapters import HTTPAdapter
from database.dblookup import DBLookup
from services.pmp_databases import PMPDatabases

httpAdapter = HTTPAdapter(pool_connections=10, pool_maxsize=100)


class CouchDBConnector:
    def __init__(self):
        self.client = None
        self.session = None
        self.databases = {}
        config = dotenv_values(os.environ.get('PMP_MICROSERVICE_CONFIG'))
        self.db_user = config.get('COUCHDB_USER')
        self.db_password = config.get('COUCHDB_PASSWORD')
        self.db_url = config.get('COUCHDB_URL')
        self.connect()

    def connect(self):
        self.client = CouchDB(self.db_user, self.db_password, url=self.db_url, connect=True, auto_renew=True,
                              adapter=httpAdapter)
        self.session = self.client.session()

        for db in PMPDatabases:
            try:
                self.databases[db] = self.client.create_database(db.value)
                self.create_views(db)
            except CloudantDatabaseException:
                self.databases[db] = self.client[db.value]

    def create_views(self, db):
        if db is PMPDatabases.lookup:
            DBLookup(self.databases[db]).create_view()


db_client = CouchDBConnector()
