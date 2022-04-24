import json
import math

from cloudant.document import Document
from flask import Blueprint, jsonify, request
from database import couchdb
from services import pmp_lookup
from services.pmp_lookup import PMPLookupCodes

lookup_blueprint = Blueprint('lookup_blueprint', __name__)


#
# Agreement Cancel Reasons
#
@lookup_blueprint.route('/pmp/agreement-cancel-reasons', methods=['GET'])
def list_agreement_cancel_reasons():
    return get_item_list(PMPLookupCodes.agreement_cancel_reasons.value)


@lookup_blueprint.route('/pmp/agreement-cancel-reasons/<lookup_id>', methods=['GET'])
def get_agreement_cancel_reasons(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/agreement-cancel-reasons/codes/<lookup_id>', methods=['GET'])
def get_agreement_cancel_reasons_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'AgreementCancelReason_PMP')
    return document


#
# Agreement Status
#
@lookup_blueprint.route('/pmp/agreement-status', methods=['GET'])
def list_agreement_status():
    return get_item_list(PMPLookupCodes.agreement_status.value)


@lookup_blueprint.route('/pmp/agreement-status/<lookup_id>', methods=['GET'])
def get_agreement_status(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/agreement-status/codes/<lookup_id>', methods=['GET'])
def get_agreement_status_by_code(lookup_id):
    document = get_item_codes(lookup_id,'AgreementStatus_PMP')
    return document


#
# Agreement Types
#
@lookup_blueprint.route('/pmp/agreement-types', methods=['GET'])
def list_agreement_types():
    return get_item_list(PMPLookupCodes.agreement_types.value)


@lookup_blueprint.route('/pmp/agreement-types/<lookup_id>', methods=['GET'])
def get_agreement_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/agreement-types/codes/<lookup_id>', methods=['GET'])
def get_agreement_types_by_code(lookup_id):
    document = get_item_codes(lookup_id,"AgreementType_PMP")
    return document


#
# APA Action Types
#
@lookup_blueprint.route('/pmp/apa-action-types', methods=['GET'])
def list_apa_action_types():
    return get_item_list(PMPLookupCodes.apa_action_types.value)


@lookup_blueprint.route('/pmp/apa-action-types/<lookup_id>', methods=['GET'])
def get_apa_action_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/apa-action-types/codes/<lookup_id>', methods=['GET'])
def get_apa_action_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, "APAActionType_PMP")
    return document


#
# APA Macro Inputs
#
@lookup_blueprint.route('/pmp/apa-macro-inputs', methods=['GET'])
def list_apa_macro_inputs():
    return get_item_list(PMPLookupCodes.apa_macro_inputs.value)


@lookup_blueprint.route('/pmp/apa-macro-inputs/<lookup_id>', methods=['GET'])
def get_apa_macro_inputs(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/apa-macro-inputs/codes/<lookup_id>', methods=['GET'])
def get_apa_macro_inputs_by_code(lookup_id):
    document = get_item_codes(lookup_id, "APAMacroInput_PMP")
    return document


#
# APA Macro Types
#
@lookup_blueprint.route('/pmp/apa-macro-types', methods=['GET'])
def list_apa_macro_types():
    return get_item_list(PMPLookupCodes.apa_macro_types.value)


@lookup_blueprint.route('/pmp/apa-macro-types/<lookup_id>', methods=['GET'])
def get_apa_macro_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/apa-macro-types/codes/<lookup_id>', methods=['GET'])
def get_apa_macro_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, "APAMacroType_PMP")
    return document


#
# Attribute Value Types
#
@lookup_blueprint.route('/pmp/attribute-value-types', methods=['GET'])
def list_attribute_value_types():
    return get_item_list(PMPLookupCodes.attribute_value_types.value)


@lookup_blueprint.route('/pmp/attribute-value-types/<lookup_id>', methods=['GET'])
def get_attribute_value_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/attribute-value-types/codes/<lookup_id>', methods=['GET'])
def get_attribute_value_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, "AttributeValueType_PMP")
    return document


#
# Billing Producer Roles
#
@lookup_blueprint.route('/pmp/billing-producer-roles', methods=['GET'])
def list_billing_producer_roles():
    return get_item_list(PMPLookupCodes.billing_producer_roles.value)


@lookup_blueprint.route('/pmp/billing-producer-roles/<lookup_id>', methods=['GET'])
def get_billing_producer_roles(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/billing-producer-roles/codes/<lookup_id>', methods=['GET'])
def get_billing_producer_roles_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'BillingProducerRole_PMP')
    return document


#
# Channels
#
@lookup_blueprint.route('/pmp/channels', methods=['GET'])
def list_channels():
    return get_item_list(PMPLookupCodes.channels.value)


@lookup_blueprint.route('/pmp/channels/<lookup_id>', methods=['GET'])
def get_channels(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/channels/codes/<lookup_id>', methods=['GET'])
def get_channels_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'Channel_PMP')
    return document


#
# Components
#
@lookup_blueprint.route('/pmp/components', methods=['GET'])
def list_components():
    return get_item_list(PMPLookupCodes.components.value)


@lookup_blueprint.route('/pmp/components/<lookup_id>', methods=['GET'])
def get_components(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/components/codes/<lookup_id>', methods=['GET'])
def get_components_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'Component_PMP')
    return document


#
# Condition Logic Opers
#
@lookup_blueprint.route('/pmp/condition-logic-opers', methods=['GET'])
def list_condition_logic_opers():
    return get_item_list(PMPLookupCodes.condition_logic_opers.value)


@lookup_blueprint.route('/pmp/condition-logic-opers/<lookup_id>', methods=['GET'])
def get_condition_logic_opers(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/condition-logic-opers/codes/<lookup_id>', methods=['GET'])
def get_condition_logic_opers_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'ConditionLogicOper_PMP')
    return document


#
# Condition Logic Types
#
@lookup_blueprint.route('/pmp/condition-logic-types', methods=['GET'])
def list_condition_logic_types():
    return get_item_list(PMPLookupCodes.condition_logic_types.value)


@lookup_blueprint.route('/pmp/condition-logic-types/<lookup_id>', methods=['GET'])
def get_condition_logic_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/condition-logic-types/codes/<lookup_id>', methods=['GET'])
def get_condition_logic_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'ConditionLogicType_PMP')
    return document


#
# Copy Clone Actions
#
@lookup_blueprint.route('/pmp/copy-clone-actions', methods=['GET'])
def list_copy_clone_actions():
    return get_item_list(PMPLookupCodes.copy_clone_actions.value)


@lookup_blueprint.route('/pmp/copy-clone-actions/<lookup_id>', methods=['GET'])
def get_copy_clone_actions(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/copy-clone-actions/codes/<lookup_id>', methods=['GET'])
def get_copy_clone_actions_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'CopyCloneAction_PMP')
    return document


#
# Export Formats
#
@lookup_blueprint.route('/pmp/export-formats', methods=['GET'])
def list_export_formats():
    return get_item_list(PMPLookupCodes.export_formats.value)


@lookup_blueprint.route('/pmp/export-formats/<lookup_id>', methods=['GET'])
def get_export_formats(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/export-formats/codes/<lookup_id>', methods=['GET'])
def get_export_formats_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'ExportFormat_PMP')
    return document


#
# File Import Types
#
@lookup_blueprint.route('/pmp/file-import-types', methods=['GET'])
def list_file_import_types():
    return get_item_list(PMPLookupCodes.file_import_types.value)


@lookup_blueprint.route('/pmp/file-import-types/<lookup_id>', methods=['GET'])
def get_file_import_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/file-import-types/codes/<lookup_id>', methods=['GET'])
def get_file_import_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'FileImportType_PMP')
    return document


#
# Item Status
#
@lookup_blueprint.route('/pmp/item-status', methods=['GET'])
def list_item_status():
    return get_item_list(PMPLookupCodes.item_status.value)


@lookup_blueprint.route('/pmp/item-status/<lookup_id>', methods=['GET'])
def get_item_status(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/item-status/codes/<lookup_id>', methods=['GET'])
def get_item_status_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'ItemStatus_PMP')
    return document


#
# Lead Follow
#
@lookup_blueprint.route('/pmp/lead-follow', methods=['GET'])
def list_lead_follow():
    return get_item_list(PMPLookupCodes.lead_follow.value)


@lookup_blueprint.route('/pmp/lead-follow/<lookup_id>', methods=['GET'])
def get_lead_follow(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/lead-follow/codes/<lookup_id>', methods=['GET'])
def get_lead_follow_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'LeadFollow_PMP')
    return document


#
# Negotiation Status
#
@lookup_blueprint.route('/pmp/negotiation-status', methods=['GET'])
def list_negotiation_status():
    return get_item_list(PMPLookupCodes.negotiation_status.value)


@lookup_blueprint.route('/pmp/negotiation-status/<lookup_id>', methods=['GET'])
def get_negotiation_status(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/negotiation-status/codes/<lookup_id>', methods=['GET'])
def get_negotiation_status_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'NegotiationStatus_PMP')
    return document


#
# Schedule Contents
#
@lookup_blueprint.route('/pmp/schedule-contents', methods=['GET'])
def list_schedule_contents():
    return get_item_list(PMPLookupCodes.schedule_contents.value)


@lookup_blueprint.route('/pmp/schedule-contents/<lookup_id>', methods=['GET'])
def get_schedule_contents(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/schedule-contents/codes/<lookup_id>', methods=['GET'])
def get_schedule_contents_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'ScheduleContent_PMP')
    return document


#
# Schedule Functions
#
@lookup_blueprint.route('/pmp/schedule-functions', methods=['GET'])
def list_schedule_functions():
    return get_item_list(PMPLookupCodes.schedule_functions.value)


@lookup_blueprint.route('/pmp/schedule-functions/<lookup_id>', methods=['GET'])
def get_schedule_functions(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/schedule-functions/codes/<lookup_id>', methods=['GET'])
def get_schedule_functions_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'ScheduleFunction_PMP')
    return document


#
# Schedule Identity Types
#
@lookup_blueprint.route('/pmp/schedule-identity-types', methods=['GET'])
def list_schedule_identity_types():
    return get_item_list(PMPLookupCodes.schedule_identity_types.value)


@lookup_blueprint.route('/pmp/schedule-identity-types/<lookup_id>', methods=['GET'])
def get_schedule_identity_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/schedule-identity-types/codes/<lookup_id>', methods=['GET'])
def get_schedule_identity_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'ScheduleIdentityType_PMP')
    return document


#
# Scheme Action Types
#
@lookup_blueprint.route('/pmp/scheme-action-types', methods=['GET'])
def list_scheme_Action_types():
    return get_item_list(PMPLookupCodes.scheme_action_types.value)


@lookup_blueprint.route('/pmp/scheme-action-types/<lookup_id>', methods=['GET'])
def get_scheme_Action_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-action-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_Action_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeActionType_PMP')
    return document


#
# Scheme Attachments
#
@lookup_blueprint.route('/pmp/scheme-attachments', methods=['GET'])
def list_scheme_Attachments():
    return get_item_list(PMPLookupCodes.scheme_attachments.value)


@lookup_blueprint.route('/pmp/scheme-attachments/<lookup_id>', methods=['GET'])
def get_scheme_Attachments(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-attachments/codes/<lookup_id>', methods=['GET'])
def get_scheme_Attachments_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeAttachment_PMP')
    return document


#
# Scheme Calc Value Types
#
@lookup_blueprint.route('/pmp/scheme-calc-value-types', methods=['GET'])
def list_scheme_calc_value_types():
    return get_item_list(PMPLookupCodes.scheme_calc_value_types.value)


@lookup_blueprint.route('/pmp/scheme-calc-value-types/<lookup_id>', methods=['GET'])
def get_scheme_calc_value_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-calc-value-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_calc_value_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeCalcValueType_PMP')
    return document


#
# Scheme Card Filters
#
@lookup_blueprint.route('/pmp/scheme-card-filters', methods=['GET'])
def list_scheme_card_filters():
    return get_item_list(PMPLookupCodes.scheme_card_filters.value)


@lookup_blueprint.route('/pmp/scheme-card-filters/<lookup_id>', methods=['GET'])
def get_scheme_card_filters(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-card-filters/codes/<lookup_id>', methods=['GET'])
def get_scheme_card_filters_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeCardFilter_PMP')
    return document


#
# Scheme Condition Types
#
@lookup_blueprint.route('/pmp/scheme-condition-types', methods=['GET'])
def list_scheme_condition_types():
    return get_item_list(PMPLookupCodes.scheme_condition_types.value)


@lookup_blueprint.route('/pmp/scheme-condition-types/<lookup_id>', methods=['GET'])
def get_scheme_condition_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-condition-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_condition_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeConditionType_PMP')
    return document


#
# Scheme Cost Types
#
@lookup_blueprint.route('/pmp/scheme-cost-types', methods=['GET'])
def list_scheme_cost_types():
    return get_item_list(PMPLookupCodes.scheme_cost_types.value)


@lookup_blueprint.route('/pmp/scheme-cost-types/<lookup_id>', methods=['GET'])
def get_scheme_cost_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-cost-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_cost_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeCostType_PMP')
    return document


#
# Scheme Create Methods
#
@lookup_blueprint.route('/pmp/scheme-create-methods', methods=['GET'])
def list_scheme_create_methods():
    return get_item_list(PMPLookupCodes.scheme_create_methods.value)


@lookup_blueprint.route('/pmp/scheme-create-methods/<lookup_id>', methods=['GET'])
def get_scheme_create_methods(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-create-methods/codes/<lookup_id>', methods=['GET'])
def get_scheme_create_methods_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeCreateMethod_PMP')
    return document


#
# Scheme Operator Types
#
@lookup_blueprint.route('/pmp/scheme-operator-types', methods=['GET'])
def list_scheme_operator_types():
    return get_item_list(PMPLookupCodes.scheme_operator_types.value)


@lookup_blueprint.route('/pmp/scheme-operator-types/<lookup_id>', methods=['GET'])
def get_scheme_operator_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-operator-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_operator_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeOperatorType_PMP')
    return document


#
# Scheme Source Types
#
@lookup_blueprint.route('/pmp/scheme-source-types', methods=['GET'])
def list_scheme_source_types():
    return get_item_list(PMPLookupCodes.scheme_source_types.value)


@lookup_blueprint.route('/pmp/scheme-source-types/<lookup_id>', methods=['GET'])
def get_scheme_source_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-source-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_source_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeSourceType_PMP')
    return document


#
# Scheme Timeframes
#
@lookup_blueprint.route('/pmp/scheme-timeframes', methods=['GET'])
def list_scheme_timeframes():
    return get_item_list(PMPLookupCodes.scheme_timeframes.value)


@lookup_blueprint.route('/pmp/scheme-timeframes/<lookup_id>', methods=['GET'])
def get_scheme_timeframes(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-timeframes/codes/<lookup_id>', methods=['GET'])
def get_scheme_timeframes_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeTimeframe_PMP')
    return document


#
# Scheme Types
#
@lookup_blueprint.route('/pmp/scheme-types', methods=['GET'])
def list_scheme_types():
    return get_item_list(PMPLookupCodes.scheme_types.value)


@lookup_blueprint.route('/pmp/scheme-types/<lookup_id>', methods=['GET'])
def get_scheme_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeType_PMP')
    return document


#
# Scheme Validation Types
#
@lookup_blueprint.route('/pmp/scheme-validation-types', methods=['GET'])
def list_scheme_validation_types():
    return get_item_list(PMPLookupCodes.scheme_validation_types.value)


@lookup_blueprint.route('/pmp/scheme-validation-types/<lookup_id>', methods=['GET'])
def get_scheme_validation_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-validation-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_validation_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeValidationType_PMP')
    return document


#
# Scheme Value Types
#
@lookup_blueprint.route('/pmp/scheme-value-types', methods=['GET'])
def list_scheme_value_types():
    return get_item_list(PMPLookupCodes.scheme_value_types.value)


@lookup_blueprint.route('/pmp/scheme-value-types/<lookup_id>', methods=['GET'])
def get_scheme_value_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/scheme-value-types/codes/<lookup_id>', methods=['GET'])
def get_scheme_value_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SchemeValueType_PMP')
    return document


#
# Suspension Reasons
#
@lookup_blueprint.route('/pmp/suspension-reasons', methods=['GET'])
def list_suspension_reasons():
    return get_item_list(PMPLookupCodes.suspension_reasons.value)


@lookup_blueprint.route('/pmp/suspension-reasons/<lookup_id>', methods=['GET'])
def get_suspension_reasons(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/suspension-reasons/codes/<lookup_id>', methods=['GET'])
def get_suspension_reasons_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SuspensionReason_PMP')
    return document


#
# System Setting Types
#
@lookup_blueprint.route('/pmp/system-setting-types', methods=['GET'])
def list_system_setting_types():
    return get_item_list(PMPLookupCodes.system_setting_types.value)


@lookup_blueprint.route('/pmp/system-setting-types/<lookup_id>', methods=['GET'])
def get_system_setting_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/system-setting-types/codes/<lookup_id>', methods=['GET'])
def get_system_setting_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'SystemSettingTypes_PMP')
    return document


#
# Virtual Flavour Actions
#
@lookup_blueprint.route('/pmp/virtual-flavour-actions', methods=['GET'])
def list_virtual_flavour_actions():
    return get_item_list(PMPLookupCodes.virtual_flavour_actions.value)


@lookup_blueprint.route('/pmp/virtual-flavour-actions/<lookup_id>', methods=['GET'])
def get_virtual_flavour_actions(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/virtual-flavour-actions/codes/<lookup_id>', methods=['GET'])
def get_virtual_flavour_actions_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'VirtualFlavourAction_PMP')
    return document


#
# Virtual Product Types
#
@lookup_blueprint.route('/pmp/virtual-product-types', methods=['GET'])
def list_virtual_product_types():
    return get_item_list(PMPLookupCodes.virtual_product_types.value)


@lookup_blueprint.route('/pmp/virtual-product-types/<lookup_id>', methods=['GET'])
def get_virtual_product_types(lookup_id):
    document = get_item(lookup_id)
    return document


@lookup_blueprint.route('/pmp/virtual-product-types/codes/<lookup_id>', methods=['GET'])
def get_virtual_product_types_by_code(lookup_id):
    document = get_item_codes(lookup_id, 'VirtualProductType_PMP')
    return document


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
    lookup_list = json.loads(lookup_id_list)
    if len(lookup_list) < 2:
        selector = {
            'code': lookup_list[0].get('code'),
            'type': type
        }
        docs = connector.lookup_database.get_query_result(selector)
        return jsonify(docs[:])
    else:
        value_list = list()
        for item in lookup_list:
            value_list.append(item.get('code'))
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
    return jsonify(view.result[:])


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
