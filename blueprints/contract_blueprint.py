import uuid
from flask import Blueprint, jsonify, request
from database import couchdb
from database.common import read, delete, create, update, search
from services.pmp_databases import PMPDatabases

contract_blueprint = Blueprint('contract_blueprint', __name__)


@contract_blueprint.route('/pmp/contracts', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.contract], request)


@contract_blueprint.route('/pmp/contracts/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.contract], item_uuid)


@contract_blueprint.route('/pmp/contracts', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.contract], request)


@contract_blueprint.route('/pmp/contracts/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.contract], item_uuid)


@contract_blueprint.route('/pmp/contracts/search', methods=['POST'])
def search_items():
    return search(couchdb.db_client.databases[PMPDatabases.contract], request)
