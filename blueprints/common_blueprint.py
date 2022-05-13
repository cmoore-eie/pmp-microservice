import uuid
from flask import Blueprint, jsonify, request
from database import couchdb
from database.common import read, delete, create, update, search
from services.pmp_databases import PMPDatabases
from services.pmptypes import PMPBaseTypes

common_blueprint = Blueprint('common_blueprint', __name__)


@common_blueprint.route('/pmp/common/base_types', methods=['GET'])
def get_base_types():
    type_dict = {}
    for key, item in PMPBaseTypes.__members__.items():
        type_dict[key] = item.value
    return jsonify(type_dict)

