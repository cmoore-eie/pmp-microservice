import math

from cloudant.document import Document
from flask import Blueprint, jsonify, request
from database import couchdb
from database.common import create, read, update, delete
from services.pmp_databases import PMPDatabases

lookup_blueprint = Blueprint('lookup_blueprint', __name__)


@lookup_blueprint.route('/pmp/lookup-types', methods=['GET'])
def list_lookup_types():
    db = couchdb.db_client.databases[PMPDatabases.lookup]
    design = db.get_design_document('_design/lookup')
    view = design.get_view('lookup-types')
    with view.custom_result(group=True) as rslt:
        return jsonify(rslt[:])


@lookup_blueprint.route('/pmp/lookup-items/type/<lookup_type>', methods=['GET'])
def list_lookup_items(lookup_type):
    db = couchdb.db_client.databases[PMPDatabases.lookup]
    if isinstance(lookup_type, str):
        connector = couchdb.db_client
        selector = {
            'type': lookup_type
        }
        docs = db.get_query_result(selector)
        return jsonify(docs[:])


@lookup_blueprint.route('/pmp/lookup-items/type/<lookup_type>/codes/<lookup_id>', methods=['GET'])
def get_lookup_items_by_code(lookup_type, lookup_id):
    document = get_item_codes(lookup_id, lookup_type)
    return document


@lookup_blueprint.route('/pmp/lookup-items/view/<view_name>', methods=['GET'])
def list_items_by_view(view_name):
    if isinstance(view_name, str):
        return get_item_list(view_name)


@lookup_blueprint.route('/pmp/lookup-items', methods=['POST'])
def create_item():
    return create(couchdb.db_client.databases[PMPDatabases.lookup], request)


@lookup_blueprint.route('/pmp/lookup-items/<item_uuid>', methods=['GET'])
def read_item(item_uuid):
    return read(couchdb.db_client.databases[PMPDatabases.lookup], item_uuid)


@lookup_blueprint.route('/pmp/lookup-items', methods=['PUT'])
def update_item():
    return update(couchdb.db_client.databases[PMPDatabases.lookup], request)


@lookup_blueprint.route('/pmp/lookup-items/<item_uuid>', methods=['DELETE'])
def delete_item(item_uuid):
    return delete(couchdb.db_client.databases[PMPDatabases.lookup], item_uuid)


def get_item(lookup_id):
    """
    Generic function to extract a single document from the database, this extracts the document
    directly as the id provided is the key to the document
    :param lookup_id:
    :return: Couchdb document
    """
    db = couchdb.db_client.databases[PMPDatabases.lookup]
    document = Document(db, lookup_id)
    document.fetch()
    return document


def get_item_codes(lookup_id_list, type):
    """
    Generic function to extract a single document or multiple documents from the database, the input is a json list of
    code : value pairs, if there is only a single item in the list this is used directly to extract the item otherwise
    a list of values is used. When there are a list of more than 25 items to be retrieved these are extracted 25 at
    a time from the database due to a query limit.
    :param lookup_id_list:
    :return: Couchdb document(s)
    """
    db = couchdb.db_client.databases[PMPDatabases.lookup]
    lookup_list = lookup_id_list.split(',')
    if len(lookup_list) < 2:
        selector = {
            'code': lookup_list[0],
            'type': type
        }
        docs = db.get_query_result(selector)
        return jsonify(docs[:])
    else:
        value_list = list()
        for item in lookup_list:
            value_list.append(item)
        if len(value_list) < 26:
            selector = {
                'code': {
                    '$in': value_list
                },
                'type': type
            }
            docs = db.get_query_result(selector)
            return jsonify(docs[:])
        else:
            return_docs = list()
            chunk_loop = int(math.ceil(len(value_list) / 25))
            for i in range(chunk_loop):
                selector = {
                    'code': {
                        '$in': chunk_list(value_list, i)
                    },
                    'type': type
                }
                docs = db.get_query_result(selector)
                for doc in docs[:]:
                    return_docs.append(doc)
            return jsonify(return_docs)


def get_item_list(view_name):
    """
    Generic function to extract a list from the database, this relies on the
    views defined in the database.
    :param view_name:
    :return: json array of metadata associated to the view
    """
    db = couchdb.db_client.databases[PMPDatabases.lookup]
    design = db.get_design_document('_design/lookup')
    view = design.get_view(view_name)
    result_items = jsonify(view.result[:])
    return_docs = list()
    for item in result_items.json:
        return_docs.append(get_item(item.get('key')))
    return jsonify(return_docs)


def chunk_list(value_list, chunk):
    chunk_size = 25
    if chunk > 0:
        chunk_start = chunk_size * chunk
        chunk_end = chunk_start + chunk_size
    else:
        chunk_start = chunk
        chunk_end = chunk_size
    if chunk_end > len(value_list):
        return value_list[chunk_start:]
    return value_list[chunk_start: chunk_end]
