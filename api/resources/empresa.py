from flask_restful import Resource, marshal_with, fields
from flask import request
import pandas as pd
from api.utils.anonimizacao import Anonimizacao
from api.models.empresa import EmpresaAnonimizada
from api.db import SessionLocal

anonimizacao = Anonimizacao()

empresa_campos = {
    'id': fields.Integer,
    'procura': fields.String,
    'cod_empresa': fields.String,
    'id_cliente': fields.Integer
}

class Empresa(Resource):
    @marshal_with(empresa_campos)
    def post(self):
        nova_empresa = request.get_json()
        df_empresa_anonimizada = pd.DataFrame([nova_empresa])
        df_empresa_anonimizada['cod_empresa'] = df_empresa_anonimizada['cod_empresa'].map(anonimizacao.hashear)
        empresa_anonimizada = EmpresaAnonimizada(**df_empresa_anonimizada.to_dict(orient='records')[0])
        
        with SessionLocal() as session:
            session.add(empresa_anonimizada)
            session.commit()
            session.refresh(empresa_anonimizada)
            print(session.query(EmpresaAnonimizada).all())

        return empresa_anonimizada, 201