from flask import Flask, jsonify, request, g

from blueprints.common_blueprint import common_blueprint
from blueprints.condition_logic_blueprint import condition_logic_blueprint
from blueprints.contract_blueprint import contract_blueprint
from blueprints.external_product_blueprint import external_product_blueprint
from blueprints.general_term_blueprint import general_term_blueprint
from blueprints.lookup_blueprint import lookup_blueprint
from blueprints.negotiation_blueprint import negotiation_blueprint
from blueprints.scheme_blueprint import scheme_blueprint
from blueprints.virtual_product_blueprint import virtual_product_blueprint

app = Flask(__name__)
app.register_blueprint(virtual_product_blueprint)
app.register_blueprint(scheme_blueprint)
app.register_blueprint(lookup_blueprint)
app.register_blueprint(condition_logic_blueprint)
app.register_blueprint(contract_blueprint)
app.register_blueprint(external_product_blueprint)
app.register_blueprint(general_term_blueprint)
app.register_blueprint(negotiation_blueprint)
app.register_blueprint(common_blueprint)


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
