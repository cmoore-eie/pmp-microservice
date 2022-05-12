import uuid
from flask import Blueprint, jsonify, request
from database import couchdb
from database.common import read, delete, create, update, search
from services.pmp_databases import PMPDatabases

condition_logic_blueprint = Blueprint('conditionlogic_blueprint', __name__)


@condition_logic_blueprint.route('/pmp/condition-logic', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.condition_logic], request)


@condition_logic_blueprint.route('/pmp/condition-logic/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.condition_logic], item_uuid)


@condition_logic_blueprint.route('/pmp/condition-logic', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.condition_logic], request)


@condition_logic_blueprint.route('/pmp/condition-logic/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.condition_logic], item_uuid)


@condition_logic_blueprint.route('/pmp/condition-logic/search', methods=['POST'])
def search_items():
    return search(couchdb.db_client.databases[PMPDatabases.condition_logic], request)
