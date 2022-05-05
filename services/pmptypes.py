from enum import Enum

type_mapping = [{'view': 'agreement-cancel-reasons', 'type': 'AgreementCancelReason_PMP'},
                {'view': 'agreement-status', 'type': 'AgreementStatus_PMP'},
                {'view': 'agreement-types', 'type': 'AgreementType_PMP'},
                {'view': 'apa-action-types', 'type': 'APAActionType_PMP'},
                {'view': 'apa-macro-inputs', 'type': 'APAMacroInput_PMP'},
                {'view': 'apa-macro-types', 'type': 'APAMacroType_PMP'},
                {'view': 'attribute-value-types', 'type': 'AttributeValueType_PMP'},
                {'view': 'billing-producer-roles', 'type': 'BillingProducerRole_PMP'},
                {'view': 'channels', 'type': 'Channel_PMP'},
                {'view': 'components', 'type': 'Component_PMP'},
                {'view': 'condition-logic-opers', 'type': 'ConditionLogicOper_PMP'},
                {'view': 'condition-logic-types', 'type': 'ConditionLogicType_PMP'},
                {'view': 'copy-clone-actions', 'type': 'CopyCloneAction_PMP'},
                {'view': 'export-formats', 'type': 'ExportFormat_PMP'},
                {'view': 'file-import-types', 'type': 'FileImportType_PMP'}]
    # general_term_attachments = 'general-term-attachments'
    # generic_clause_types = 'generic-clause-types'
    # generic_list_types = 'generic-list-types'
    # generic_multiplicity = 'generic-multiplicity'
    # generic_subprod_styles = 'generic-subprod-styles'
    # item_status = 'item-status'
    # lead_follow = 'lead-follow'
    # negotiation_status = 'negotiation-status'
    # schedule_contents = 'schedule-contents'
    # schedule_functions = 'schedule-functions'
    # schedule_identity_types = 'schedule-identity-types'
    # scheme_action_types = 'scheme-action-types'
    # scheme_attachments = 'scheme-attachments'
    # scheme_calc_value_types = 'scheme-calc-value-types'
    # scheme_card_filters = 'scheme-card-filters'
    # scheme_condition_types = 'scheme-condition-types'
    # scheme_cost_types = 'scheme-cost-types'
    # scheme_create_methods = 'scheme-create-methods'
    # scheme_operator_types = 'scheme-operator-types'
    # scheme_source_types = 'scheme-source-types'
    # scheme_timeframes = 'scheme-timeframes'
    # scheme_types = 'scheme-types'
    # scheme_validation_types = 'scheme-validation-types'
    # scheme_value_types = 'scheme-value-types'
    # suspension_reasons = 'suspension-reasons'
    # system_setting_types = 'system-setting-types'
    # virtual_flavour_actions = 'virtual-flavour-actions'
    # virtual_product_types = 'virtual-product-types'}]


class PMPTypes(Enum):
    condition_logic = 'Condition Logic'
    scheme = 'Scheme'
    virtual_product = 'Virtual Product'
    virtual_product_category = 'Virtual Product Category'
    virtual_product_contract = 'Virtual Product Contract'
    virtual_product_flavour = 'Virtual Product Flavour'
    virtual_product_line = 'Virtual Product Line'
    lookup_apa_action_type = 'APAActionType_PMP'
    lookup_virtual_product_type = 'VirtualProductType_PMP'
