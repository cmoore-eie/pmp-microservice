from enum import Enum


class PMPDatabases(Enum):
    condition_logic = 'pmp-condition-logic'
    contract = 'pmp-contract'
    coverage_dependancy = 'pmp-coverage-dependancy'
    external_product = 'pmp-external-product'
    general_term = 'pmp-general-term'
    lookup = 'pmp-lookup'
    negotiation = 'pmp-negotiation'
    scheme = 'pmp-scheme'
    virtual_product = 'pmp-virtual-product'

