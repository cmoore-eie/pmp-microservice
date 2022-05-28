class DBVirtualProduct:

    def __init__(self, db):
        self.db = db

    def create_view(self):
        self.db.create_document(self.get_view())

    def get_view(self):
        return {
            "_id": "_design/virtualproduct",
            "language": "javascript",
            "views": {
                "virtual_product": {
                    "map": "function (doc) {\n  emit(doc._id, 1);\n}"
                },
                "virtual_product_effective": {
                    "map": "function (doc) {\n  var effective_date = doc.effective_date;\n  var year = parseInt(effective_date.substr(0, 4));\n  var month = parseInt(effective_date.substr(5, 2), 10);\n  var day = parseInt(effective_date.substr(8, 2), 10);\n  emit([year, month, day], doc._id);\n}"
                },
                "virtual_product_draft": {
                    "map": "function (doc) {\n  if(doc.item_status == \"draft\"){\n    emit(doc._id, doc.item_status)\n  }\n}"
                },
                "virtual_product_approved": {
                    "map": "function (doc) {\n  if(doc.item_status == \"approved\"){\n    emit(doc._id, doc.item_status)\n  }\n}"
                },
                "virtual_product_stage": {
                    "map": "function (doc) {\n  if(doc.item_status == \"stage\"){\n    emit(doc._id, doc.item_status)\n  }\n}"
                }
            }
        }
