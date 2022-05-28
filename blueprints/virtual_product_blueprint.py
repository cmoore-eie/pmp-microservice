import json

from cloudant.document import Document
from flask import Blueprint, jsonify, request
from flask_restful import abort

from database import couchdb
from database.common import delete, update, read, create, search, search_by_effective
from services.pmp_databases import PMPDatabases
from services.pmptypes import PMPDesignDocument

virtual_product_blueprint = Blueprint('virtualproduct_blueprint', __name__)


@virtual_product_blueprint.route('/pmp/virtual-products', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.virtual_product], request)


@virtual_product_blueprint.route('/pmp/virtual-products/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.virtual_product], item_uuid)


@virtual_product_blueprint.route('/pmp/virtual-products/search', methods=['POST'])
def search_items():
    return search(couchdb.db_client.databases[PMPDatabases.virtual_product], request)

@virtual_product_blueprint.route('/pmp/virtual-products/search-effective', methods=['POST'])
def search_effective():
    view_document = f'_design/{PMPDesignDocument.virtual_product.value}'
    view_name = 'effective_date'
    return search_by_effective(couchdb.db_client.databases[PMPDatabases.virtual_product], view_document, view_name
                               , request)


@virtual_product_blueprint.route('/pmp/virtual-products', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.virtual_product], request)


@virtual_product_blueprint.route('/pmp/virtual-products/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.virtual_product], item_uuid)
