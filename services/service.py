from cloudant import CouchDB
from cloudant.error import CloudantDatabaseException
from flask import Flask, jsonify, request, g
from requests.adapters import HTTPAdapter

from blueprints.lookup_blueprint import lookup_blueprint
from blueprints.scheme_blueprint import scheme_blueprint
from blueprints.virtual_product_blueprint import virtual_product_blueprint
from services.pmp_databases import PMPDatabases

app = Flask(__name__)
app.register_blueprint(virtual_product_blueprint)
app.register_blueprint(scheme_blueprint)
app.register_blueprint(lookup_blueprint)


@app.route("/")
def auth():
    # print("The raw Authorization header")
    # print(request.environ["HTTP_AUTHORIZATION"])
    # print("Flask's Authorization header")
    # print(request.authorization)
    return ""


@app.route('/pmp')
def pmp_microservice():
    return jsonify({'Hello': 'PMP!'})



if __name__ == '__main__':
    app.run()
