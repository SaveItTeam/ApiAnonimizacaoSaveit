from flask_restful import Resource, marshal_with, fields
from flask import request
import pandas as pd
from api.utils.anonimizacao import Anonimizacao
from api.models.admin import AdminAnonimizado
from api.db import SessionLocal

admin_campos = {
    'id': fields.Integer,
    'cargo': fields.String,
    'nome_empresa': fields.String,
    'nome_admin': fields.String,
    'senha': fields.String
}

class Admin(Resource):
    @marshal_with(admin_campos)
    def post(self):
        novo_admin = request.get_json()
        df_admin_anonimizado = pd.DataFrame([novo_admin])
        df_admin_anonimizado['cargo'] = df_admin_anonimizado['cargo'].map(Anonimizacao.generalizar_cargo)
        df_admin_anonimizado['nome_empresa'] = df_admin_anonimizado['nome_empresa'].map(Anonimizacao.criptografar)
        df_admin_anonimizado['nome_admin'] = df_admin_anonimizado['nome_admin'].map(Anonimizacao.criptografar)
        df_admin_anonimizado['senha'] = df_admin_anonimizado['senha'].map(Anonimizacao.hashear)
        admin_anonimizado = AdminAnonimizado(**df_admin_anonimizado.to_dict(orient='records')[0])

        with SessionLocal() as session:
            session.add(admin_anonimizado)
            session.commit()
            session.refresh(admin_anonimizado)
            print(session.query(AdminAnonimizado).all())
    
        # CONSIDERAR TROCAR RETORNO PARA SENHA CRIPTOGRAFADA
        return admin_anonimizado, 201