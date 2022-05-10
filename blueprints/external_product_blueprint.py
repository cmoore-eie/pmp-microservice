import uuid
from flask import Blueprint, jsonify, request
from database import couchdb
from database.common import create, read, update, delete
from services.pmp_databases import PMPDatabases

external_product_blueprint = Blueprint('external_product_blueprint', __name__)


@external_product_blueprint.route('/pmp/external-products', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.external_product], request)


@external_product_blueprint.route('/pmp/external-products/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.external_product], item_uuid)


@external_product_blueprint.route('/pmp/external-products', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.external_product], request)


@external_product_blueprint.route('/pmp/external-products/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.external_product], item_uuid)
