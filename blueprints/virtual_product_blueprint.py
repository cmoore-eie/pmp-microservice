import json

from cloudant.document import Document
from flask import Blueprint, jsonify, request
from flask_restful import abort

from database import couchdb
from database.common import delete, update, read, create
from services.pmp_databases import PMPDatabases

virtual_product_blueprint = Blueprint('virtualproduct_blueprint', __name__)


@virtual_product_blueprint.route('/pmp/virtual-products', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.scheme], request)


@virtual_product_blueprint.route('/pmp/virtual-products/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.scheme], item_uuid)


@virtual_product_blueprint.route('/pmp/virtual-products', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.scheme], request)


@virtual_product_blueprint.route('/pmp/virtual-products/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.scheme], item_uuid)
