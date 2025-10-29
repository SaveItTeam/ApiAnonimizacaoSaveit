from flask_restful import Resource, marshal_with, fields
from flask import request
from api.utils.anonimizacao import Anonimizacao
import pandas as pd
from api.models.endereco import EnderecoAnonimizado
from api.db import SessionLocal

endereco_campos = {
    'id': fields.Integer,
    'cep': fields.String,
    'cep_rua': fields.String,
    'cep_bairro': fields.String,
    'cep_cidade': fields.String,
    'cep_estado': fields.String,
    'cep_pais': fields.String,
    'cep_complemento': fields.String,
    'cep_rua_numero': fields.Integer
}

class Endereco(Resource):
    @marshal_with(endereco_campos)
    def post(self):
        novo_endereco = request.get_json()
        df_endereco_anonimizado = pd.DataFrame([novo_endereco]).loc[:, ['id', 'cep', 'cep_rua', 'cep_bairro', 'cep_estado', 'cep_pais']]
        df_endereco_anonimizado['cep'] = df_endereco_anonimizado['cep'].map(Anonimizacao.hashear)
        df_endereco_anonimizado['cep_rua'] = df_endereco_anonimizado['cep_rua'].map(Anonimizacao.mascarar)
        df_endereco_anonimizado['cep_bairro'] = df_endereco_anonimizado['cep_bairro'].map(Anonimizacao.mascarar)
        endereco_anonimizado = EnderecoAnonimizado(**df_endereco_anonimizado.to_dict(orient='records')[0])
        
        with SessionLocal() as session:
            session.add(endereco_anonimizado)
            session.commit()
            session.refresh(endereco_anonimizado)
            print(session.query(EnderecoAnonimizado).all())

        return endereco_anonimizado, 201