import json

from cloudant.document import Document
from flask import Blueprint, jsonify, request

from database import couchdb
from services.http_status import HttpStatus

virtual_product_blueprint = Blueprint('virtualproduct_blueprint', __name__)


@virtual_product_blueprint.route('/pmp/virtualproduct/<virtual_product_id>', methods=['GET'])
def get_virtual_product(virtual_product_id):
    document = get_document(virtual_product_id)
    return document


@virtual_product_blueprint.route('/pmp/virtualproduct', methods=['POST'])
def create_virtual_product():
    if request.data is not None and request.is_json:
        data = json.loads(request.data)
        connector = couchdb.db_client
        db = connector.virtual_product_database
        db.create_document(data)
        return '', HttpStatus.created_201.value
    return '',HttpStatus.bad_request_400.value


@virtual_product_blueprint.route('/pmp/virtualproduct/<virtual_product_id>', methods=['DELETE'])
def delete_virtual_product(virtual_product_id):
    connector = couchdb.db_client
    db = connector.virtual_product_database
    document = get_document(virtual_product_id)
    document.fetch()
    document.delete()
    return jsonify({'Delete Virtual Product': virtual_product_id})


@virtual_product_blueprint.route('/pmp/virtualproducts', methods=['GET'])
def find_virtual_products():
    return jsonify({'Hello Virtual Product': 'All'})


def get_document(lookup_id):
    connector = couchdb.db_client
    document = Document(connector.virtual_product_database, lookup_id)
    document.fetch()
    return document