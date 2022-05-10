import uuid
from flask import Blueprint, jsonify, request
from database import couchdb
from database.common import create, read, update, delete
from services.pmp_databases import PMPDatabases

general_term_blueprint = Blueprint('general_term_blueprint', __name__)


@general_term_blueprint.route('/pmp/general-terms', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.general_term], request)


@general_term_blueprint.route('/pmp/general-terms/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.general_term], item_uuid)


@general_term_blueprint.route('/pmp/general-terms', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.general_term], request)


@general_term_blueprint.route('/pmp/general-terms/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.general_term], item_uuid)
