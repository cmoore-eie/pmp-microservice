import uuid
from flask import Blueprint, jsonify, request
from database import couchdb
from database.common import create, read, update, delete, search
from services.pmp_databases import PMPDatabases

negotiation_blueprint = Blueprint('negotiation_blueprint', __name__)


@negotiation_blueprint.route('/pmp/negotiations', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.negotiation], request)


@negotiation_blueprint.route('/pmp/negotiations/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.negotiation], item_uuid)


@negotiation_blueprint.route('/pmp/negotiations', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.negotiation], request)


@negotiation_blueprint.route('/pmp/negotiations/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.negotiation], item_uuid)


@negotiation_blueprint.route('/pmp/negotiations/search', methods=['POST'])
def search_items():
    return search(couchdb.db_client.databases[PMPDatabases.negotiation], request)
