from cloudant.document import Document
from flask import Blueprint, jsonify
from database import couchdb

lookup_blueprint = Blueprint('lookup_blueprint', __name__)


@lookup_blueprint.route('/pmp/APAActionTypes', methods=['GET'])
def find_apa_action_types():
    return get_item_list('apa_action_type')


@lookup_blueprint.route('/pmp/APAActionType/<lookup_id>', methods=['GET'])
def get_apa_action_type(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/AgreementStatuses', methods=['GET'])
def find_agreement_statuses():
    return get_item_list('agreement_status')

@lookup_blueprint.route('/pmp/AgreementStatus/<lookup_id>', methods=['GET'])
def get_agreement_status(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/AgreementTypes', methods=['GET'])
def find_agreement_types():
    return get_item_list('agreement_type')


@lookup_blueprint.route('/pmp/AgreementType/<lookup_id>', methods=['GET'])
def get_agreement_type(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/ItemStatuses', methods=['GET'])
def find_item_statuses():
    return get_item_list('item_status')


@lookup_blueprint.route('/pmp/ItemStatus/<lookup_id>', methods=['GET'])
def get_item_status(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/VirtualFlavourActions', methods=['GET'])
def find_virtual_flavour_actions():
    return get_item_list('virtual_flavour_action')


@lookup_blueprint.route('/pmp/VirtualFlavourAction/<lookup_id>', methods=['GET'])
def get_virtual_flavour_action(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/VirtualProductTypes', methods=['GET'])
def find_virtual_product_types():
    return get_item_list('virtual_product_type')


@lookup_blueprint.route('/pmp/VirtualProductType/<lookup_id>', methods=['GET'])
def get_virtual_product_type(lookup_id):
    document = get_item(lookup_id)
    return document


def get_item(lookup_id):
    connector = couchdb.db_client
    document = Document(connector.lookup_database, lookup_id)
    document.fetch()
    return document
    # connector = couchdb.db_client
    # design = connector.lookup_database.get_design_document('_design/lookup')
    # view = design.get_view(view_name)
    # with view.custom_result(key=lookup_id) as rslt:
    #     item = rslt[:]
    #     if len(item) == 1:
    #         return item[0]


def get_item_list(view_name):
    connector = couchdb.db_client
    design = connector.lookup_database.get_design_document('_design/lookup')
    view = design.get_view(view_name)
    return jsonify(view.result[:])
