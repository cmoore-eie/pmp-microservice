import uuid

from cloudant.document import Document
from flask import jsonify


def create(db, request):
    if request.content_type == 'application/json':
        json = request.json
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


def read(db, item_uuid):
    if isinstance(item_uuid, str):
        with Document(db, item_uuid) as document:
            try:
                document.fetch()
                return document
            except:
                resp = jsonify(f'Document does not exist : {item_uuid}')
                resp.status_code = 400
                return resp


def update(db, request):
    if request.content_type == 'application/json':
        json = request.json
        document = read(db, json['_id'])
        for key, value in json.items():
            if not key.startswith('_'):
                if document[key] != value:
                    document[key] = value
        document.save()
        resp = jsonify(json)
        resp.status_code = 200
        return resp
    else:
        resp = jsonify('Unsupported Content Type')
        resp.status_code = 400
        return resp


def delete(db, item_uuid):
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
