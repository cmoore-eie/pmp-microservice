import uuid
from cloudant.document import Document
from flask import Blueprint, jsonify, request
from database import couchdb

condition_logic_blueprint = Blueprint('conditionlogic_blueprint', __name__)


@condition_logic_blueprint.route('/pmp/condition-logic', methods=['GET'])
def find_virtual_products():
    return jsonify({'Hello Condition Logic': 'All'})


@condition_logic_blueprint.route('/pmp/condition-logic', methods=['POST'])
def update_lookup_items():
    if request.content_type == 'application/json':
        json = request.json
        db = couchdb.db_client.condition_logic_database
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


@condition_logic_blueprint.route('/pmp/condition-logic/<condition_logic_id>', methods=['GET'])
def get_condition_logic(condition_logic_id):
    document = get_document(condition_logic_id)
    return document


@condition_logic_blueprint.route('/pmp/condition-logic/id/<condition_logic_id>', methods=['DELETE'])
def remove_condition_logic(lookup_id):
    connector = couchdb.db_client
    db = couchdb.db_client.condition_logic_database
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


def get_document(lookup_id):
    connector = couchdb.db_client
    document = Document(connector.condition_logic_database, lookup_id)
    document.fetch()
    return document
