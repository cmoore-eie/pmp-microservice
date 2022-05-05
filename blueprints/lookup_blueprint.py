import math
import uuid

from cloudant.document import Document
from flask import Blueprint, jsonify, request
from database import couchdb

lookup_blueprint = Blueprint('lookup_blueprint', __name__)


#
# General
#
@lookup_blueprint.route('/pmp/lookup-types', methods=['GET'])
def list_lookup_types():
    connector = couchdb.db_client
    design = connector.lookup_database.get_design_document('_design/lookup')
    view = design.get_view('lookup-types')
    with view.custom_result(group=True) as rslt:
        return jsonify(rslt[:])


@lookup_blueprint.route('/pmp/lookup-items/type/<lookup_type>', methods=['GET'])
def list_lookup_items(lookup_type):
    if isinstance(lookup_type, str):
        connector = couchdb.db_client
        selector = {
            'type': lookup_type
        }
        docs = connector.lookup_database.get_query_result(selector)
        return jsonify(docs[:])


@lookup_blueprint.route('/pmp/lookup-items/type/<lookup_type>/codes/<lookup_id>', methods=['GET'])
def get_lookup_items_by_code(lookup_type, lookup_id):
    document = get_item_codes(lookup_id, lookup_type)
    return document


@lookup_blueprint.route('/pmp/lookup-items/view/<view_name>', methods=['GET'])
def list_lookup_items_by_view(view_name):
    if isinstance(view_name, str):
        return get_item_list(view_name)


@lookup_blueprint.route('/pmp/lookup-items/id/<lookup_id>', methods=['GET'])
def get_lookup_items(lookup_id):
    if isinstance(lookup_id, str):
        db = couchdb.db_client.lookup_database
        with Document(db, lookup_id) as document:
            try:
                document.fetch()
                return document
            except:
                resp = jsonify(f'Document does not exist : {lookup_id}')
                resp.status_code = 400
                return resp


@lookup_blueprint.route('/pmp/lookup-items', methods=['POST'])
def create_lookup_items():
    if request.content_type == 'application/json':
        json = request.json
        db = couchdb.db_client.lookup_database
        if '_id' not in json:
            json['_id'] = str(uuid.uuid4())
        db.create_document(json)
        resp = jsonify(json)
        resp.status_code = 200
        return resp
    else:
        resp = jsonify('Unsupported Content Type')
        resp.status_code = 400
        return resp


@lookup_blueprint.route('/pmp/lookup-items', methods=['PUT'])
def update_lookup_items():
    if request.content_type == 'application/json':
        json = request.json
        db = couchdb.db_client.lookup_database
        document = get_item(json['_id'])
        document['name'] = json['name']
        document.save()
        resp = jsonify(json)
        resp.status_code = 200
        return resp
    else:
        resp = jsonify('Unsupported Content Type')
        resp.status_code = 400
        return resp


@lookup_blueprint.route('/pmp/lookup-items/id/<lookup_id>', methods=['DELETE'])
def remove_lookup_items(lookup_id):
    connector = couchdb.db_client
    db = couchdb.db_client.lookup_database
    if lookup_id in db:
        with Document(db, lookup_id) as document:
            document['_deleted'] = True
            resp = jsonify(f'Document deleted : {lookup_id}')
            resp.status_code = 200
            return resp
    else:
        resp = jsonify('Invalid Document')
        resp.status_code = 400
        return resp


def get_item(lookup_id):
    """
    Generic function to extract a single document from the database, this extracts the document
    directly as the id provided is the key to the document
    :param lookup_id:
    :return: Couchdb document
    """
    connector = couchdb.db_client
    document = Document(connector.lookup_database, lookup_id)
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
    connector = couchdb.db_client
    lookup_list = lookup_id_list.split(',')
    if len(lookup_list) < 2:
        selector = {
            'code': lookup_list[0],
            'type': type
        }
        docs = connector.lookup_database.get_query_result(selector)
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
            docs = connector.lookup_database.get_query_result(selector)
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
                docs = connector.lookup_database.get_query_result(selector)
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
    connector = couchdb.db_client
    design = connector.lookup_database.get_design_document('_design/lookup')
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
