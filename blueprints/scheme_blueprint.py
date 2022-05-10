from flask import Blueprint, jsonify, request

from database import couchdb
from database.common import read, delete, update, create
from services.pmp_databases import PMPDatabases

scheme_blueprint = Blueprint('scheme_blueprint', __name__)


@scheme_blueprint.route('/pmp/schemes', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.scheme], request)


@scheme_blueprint.route('/pmp/schemes/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.scheme], item_uuid)


@scheme_blueprint.route('/pmp/schemes', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.scheme], request)


@scheme_blueprint.route('/pmp/schemes/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.scheme], item_uuid)