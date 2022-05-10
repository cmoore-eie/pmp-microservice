import uuid
from flask import Blueprint, jsonify, request
from database import couchdb
from database.common import create, read, update, delete
from services.pmp_databases import PMPDatabases

coverage_dependancy_blueprint = Blueprint('coverage_dependancy_blueprint', __name__)


@coverage_dependancy_blueprint.route('/pmp/coverage-dependancy', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.contract], request)


@coverage_dependancy_blueprint.route('/pmp/coverage-dependancy/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.contract], item_uuid)


@coverage_dependancy_blueprint.route('/pmp/coverage-dependancy', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.contract], request)


@coverage_dependancy_blueprint.route('/pmp/coverage-dependancy/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.contract], item_uuid)
