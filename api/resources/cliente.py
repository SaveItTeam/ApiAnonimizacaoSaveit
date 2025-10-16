from flask_restful import Resource, fields, marshal_with
from flask import request
import pandas as pd
from api.utils.anonimizacao import Anonimizacao
from api.models.cliente import ClienteAnonimizado
from api.db import SessionLocal

cliente_campos = {
    'id': fields.Integer,
    'cnpj': fields.String,
    'nome': fields.String,
    'email': fields.String,
    'senha': fields.String,
    'telefone': fields.String,
    'tipo': fields.Integer,
    'tipo_venda': fields.String,
    'id_empresa': fields.Integer,
    'id_endereco': fields.Integer,
    'id_industria': fields.Integer
}

class Cliente(Resource):
    @marshal_with(cliente_campos)
    def post(self):
        novo_cliente = request.get_json()
        df_cliente_anonimizado = pd.DataFrame([novo_cliente])
        df_cliente_anonimizado['cnpj'] = df_cliente_anonimizado['cnpj'].map(Anonimizacao.hashear)
        df_cliente_anonimizado['nome'] = df_cliente_anonimizado['nome'].map(Anonimizacao.criptografar)
        df_cliente_anonimizado['email_dominio'] = df_cliente_anonimizado['email'].map(Anonimizacao.pegar_dominio)
        df_cliente_anonimizado['email'] = df_cliente_anonimizado['email'].map(Anonimizacao.hashear)
        df_cliente_anonimizado['senha'] = df_cliente_anonimizado['senha'].map(Anonimizacao.hashear)
        df_cliente_anonimizado['telefone'] = df_cliente_anonimizado['telefone'].map(Anonimizacao.mascarar)
        cliente_anonimizado = ClienteAnonimizado(**df_cliente_anonimizado.to_dict(orient='records')[0])
        
        with SessionLocal() as session:
            session.add(cliente_anonimizado)
            session.commit()
            session.refresh(cliente_anonimizado)
            print(session.query(ClienteAnonimizado).all())
        
        return cliente_anonimizado, 201