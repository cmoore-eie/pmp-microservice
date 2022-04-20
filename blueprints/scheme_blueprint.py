from flask import Blueprint, jsonify

scheme_blueprint = Blueprint('scheme_blueprint', __name__)


@scheme_blueprint.route('/pmp/scheme/<scheme_id>', methods=['GET'])
def scheme(scheme_id):
    return jsonify({'Hello Scheme': scheme_id})


@scheme_blueprint.route('/pmp/schemes', methods=['GET'])
def schemes():
    return jsonify({'Hello schemes': 'All'})