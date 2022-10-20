import datetime
import uuid
from cloudant.document import Document
from cloudant.error import CloudantDocumentException
from flask import jsonify

from constants import APPLICATION_JSON, UNSUPPORTED_CONTENT_TYPE


def create(db, request):
    """
    Create a new item in the database provided, the item must be a json string. The _id of the document should
    be set, if no the item_identifier is used otherwise a new _id is created. Effective and Expiration dates
    have their counterpart internal fields set, these are used during selection.
    :param db:
    :param request:
    :return:
    """
    if request.content_type == APPLICATION_JSON:
        json = request.json
        if '_id' not in json:
            if 'item_identifier' in json:
                json['_id'] = json['item_identifier']
            else:
                json['_id'] = str(uuid.uuid4())
                json['item_identifier'] = json['_id']
        if 'effective_date' in json:
            json['effective_date_internal'] = datetime.datetime.fromisoformat(json['effective_date']).timestamp()
        if 'expiration_date' in json and json['expiration_date'] is not None:
            json['expiration_date_internal'] = datetime.datetime.fromisoformat(json['expiration_date']).timestamp()

        json['create_time'] = datetime.datetime.now().isoformat()
        db.create_document(json)
        resp = jsonify(json)
        resp.status_code = 200
        return resp
    else:
        resp = jsonify(UNSUPPORTED_CONTENT_TYPE)
        resp.status_code = 400
        return resp


def read(db, item_uuid):
    """
    Read an item from the database using the _id uuid
    :param db:
    :param item_uuid:
    :return:
    """
    if isinstance(item_uuid, str):
        with Document(db, item_uuid) as document:
            try:
                document.fetch()
                return document
            except CloudantDocumentException:
                resp = jsonify(f'Document does not exist : {item_uuid}')
                resp.status_code = 400
                return resp


def update(db, request):
    """
    Updates an existing item in the database, Only the fields specified in the json input are checked
    for changes. _id and _rev attributes will not be checked.
    :param db:
    :param request:
    :return:
    """
    if request.content_type == APPLICATION_JSON:
        json = request.json
        document = read(db, json['_id'])
        for key, value in json.items():
            if not key.startswith('_') and document[key] != value:
                document[key] = value
        json['update_time'] = datetime.datetime.now().isoformat()
        document.save()
        resp = jsonify(json)
        resp.status_code = 200
        return resp
    else:
        resp = jsonify(UNSUPPORTED_CONTENT_TYPE)
        resp.status_code = 400
        return resp


def delete(db, item_uuid):
    """
    Delete an item from the supplied database that has the _id of the provided uuid
    :param db:
    :param item_uuid:
    :return:
    """
    if item_uuid in db:
        with Document(db, item_uuid) as document:
            document['_deleted'] = True
            resp = jsonify(f'Document deleted : {item_uuid}')
            resp.status_code = 200
            return resp
    else:
        resp = jsonify('Invalid Document')
        resp.status_code = 400
        return resp


def find(db, selector):
    """
    Find extracts all the documents from the given database what match the criteria in the selector,
    this makes use of bookmarks to repeatedly extract results.
    :param db:
    :param selector:
    :return:
    """
    return_docs = list()
    result = db.get_query_result(selector, raw_result=True)
    while len(result['docs']) > 0:
        bookmark = result['bookmark']
        return_docs.extend(result['docs'])
        result = db.get_query_result(selector, raw_result=True, bookmark=bookmark)
    return jsonify(return_docs)


def find_all(db):
    """
    Find extracts all the documents from the given database what match the criteria in the selector,
    this makes use of bookmarks to repeatedly extract results.
    :param db:
    :param selector:
    :return:
    """
    return_docs = list()
    result = db.all_docs(include_docs=True)
    for row in result.get('rows'):
        return_docs.append(row['doc'])
    return jsonify(return_docs)


def search(db, request):
    """
    Searches the provided database for records that match the criteria supplied as a json string.
    Search gets the criteria via the data in the request and builds the selector
    to pass to the find function.
    :param db:
    :param request:
    :return:
    """
    if request.content_type == APPLICATION_JSON:
        if len(request.data) == 0:
            return find_all(db)
        else:
            json = request.json
            selector = {}
            for key, value in json.items():
                selector[key] = value
            return find(db, selector)
    else:
        resp = jsonify(UNSUPPORTED_CONTENT_TYPE)
        resp.status_code = 400
        return resp


def search_by_effective(db, request):
    """
    Searches the provided database for records that match the criteria supplied as a json string.
    Search gets the criteria via the data in the request and builds the selector
    to pass to the find function.
    :param db:
    :param request:
    :return:
    """
    if request.content_type == APPLICATION_JSON:
        if len(request.data) == 0:
            return find_all(db)
        else:
            json = request.json
            selector = {}
            date_selector = {}
            if 'effective_date' in json:
                date = datetime.date((json['effective_date']))
                date_selector['effective_date_internal'] = {'$gte': date}
            for key, value in json.items():
                selector[key] = value
            return find(db, selector)
    else:
        resp = jsonify('Unsupported Content Type')
        resp.status_code = 400
        return resp


def search_all(db):
    return find_all(db)
