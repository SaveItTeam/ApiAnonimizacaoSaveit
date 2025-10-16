from flask import Flask
from flask_restful import Api
from api.resources.admin import Admin
from api.resources.empresa import Empresa
from api.resources.endereco import Endereco
from api.resources.funcionario import Funcionario
from api.resources.industria import Industria
from api.resources.pagamento import Pagamento
from api.resources.plano import Plano
from api.resources.cliente import Cliente

def create_app():
    app = Flask(__name__)
    api = Api(app)
    @app.route('/')
    def home():
        return """<h1>API ta rodando 🔥</h1>
                  <p>vambora</p>"""

# Rotas RESTful
    api.add_resource(Admin, '/api/admin')
    api.add_resource(Empresa, '/api/empresa')
    api.add_resource(Endereco, '/api/endereco')
    api.add_resource(Funcionario, '/api/funcionario')
    api.add_resource(Industria, '/api/industria')
    api.add_resource(Pagamento, '/api/pagamento')
    api.add_resource(Plano, '/api/plano')
    api.add_resource(Cliente, '/api/cliente')
    
    return app