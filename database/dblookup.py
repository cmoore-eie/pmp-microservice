class DBLookup:

    def __init__(self, db):
        self.db = db

    def create_view(self):
        self.db.create_document(self.get_view())

    def get_view(self):
        return {
            "_id": "_design/lookup",
            "views": {
                "agreement-cancel-reasons": {
                    "map": "function(doc) {\n  if(doc.type == \"AgreementCancelReason_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "agreement-status": {
                    "map": "function(doc) {\n  if(doc.type == \"AgreementStatus_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "agreement-types": {
                    "map": "function(doc) {\n  if(doc.type == \"AgreementType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "apa-action-types": {
                    "map": "function(doc) {\n  if(doc.type == \"APAActionType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "apa-macro-inputs": {
                    "map": "function(doc) {\n  if(doc.type == \"APAMacroInput_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "apa-macro-types": {
                    "map": "function(doc) {\n  if(doc.type == \"APAMacroType_PMP\"){\n   emit(doc._id, doc.code)\n  }\n}"
                },
                "attribute-value-types": {
                    "map": "function(doc) {\n  if(doc.type == \"AttributeValueType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "billing-producer-roles": {
                    "map": "function(doc) {\n  if(doc.type == \"BillingProducerRole_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "channels": {
                    "map": "function(doc) {\n  if(doc.type == \"Channel_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "components": {
                    "map": "function(doc) {\n  if(doc.type == \"Component_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "condition-logic-opers": {
                    "map": "function(doc) {\n  if(doc.type == \"ConditionLogicOper_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "condition-logic-types": {
                    "map": "function(doc) {\n  if(doc.type == \"ConditionLogicType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "copy-clone-actions": {
                    "map": "function(doc) {\n  if(doc.type == \"CopyCloneAction_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "export-formats": {
                    "map": "function(doc) {\n  if(doc.type == \"ExportFormat_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "file-import-types": {
                    "map": "function(doc) {\n  if(doc.type == \"FileImportType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "item-status": {
                    "map": "function(doc) {\n  if(doc.type == \"ItemStatus_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "lead-follow": {
                    "map": "function(doc) {\n  if(doc.type == \"LeadFollow_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "negotiation-status": {
                    "map": "function(doc) {\n  if(doc.type == \"NegotiationStatus_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "schedule-contents": {
                    "map": "function(doc) {\n  if(doc.type == \"ScheduleContent_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "schedule-functions": {
                    "map": "function(doc) {\n  if(doc.type == \"ScheduleFunction_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "schedule-identity-types": {
                    "map": "function(doc) {\n  if(doc.type == \"ScheduleIdentityType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-action-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeActionType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-attachments": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeAttachment_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-calc-value-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeCalcValueType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-card-filters": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeCardFilter_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-condition-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeConditionType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-cost-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeCostType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-create-methods": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeCreateMethod_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-operator-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeOperatorType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-source-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeSourceType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-timeframes": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeTimeframe_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-validation-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeValidationType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "scheme-value-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SchemeValueType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "suspension-reasons": {
                    "map": "function(doc) {\n  if(doc.type == \"SuspensionReason_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "system-setting-types": {
                    "map": "function(doc) {\n  if(doc.type == \"SystemSettingTypes_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "virtual-flavour-actions": {
                    "map": "function(doc) {\n  if(doc.type == \"VirtualFlavourAction_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "virtual-product-types": {
                    "map": "function(doc) {\n  if(doc.type == \"VirtualProductType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "lookup-types": {
                    "map": "function (doc) {\n  emit(doc.type, 1);\n}",
                    "reduce": "_sum"
                },
                "general-term-attachments": {
                    "map": "function(doc) {\n  if(doc.type == \"GeneralTermAttachment_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "generic-clause-types": {
                    "map": "function(doc) {\n  if(doc.type == \"GenericClauseType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "generic-list-types": {
                    "map": "function(doc) {\n  if(doc.type == \"GenericListType_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "generic-multiplicity": {
                    "map": "function(doc) {\n  if(doc.type == \"GenericMultiplicity_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                },
                "generic-subprod-styles": {
                    "map": "function(doc) {\n  if(doc.type == \"GenericSubprodStyle_PMP\"){\n    emit(doc._id, doc.code)\n  }\n}"
                }
            }
        }
