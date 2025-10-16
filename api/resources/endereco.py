from flask_restful import Resource, marshal_with, fields
from flask import request
from api.utils.anonimizacao import Anonimizacao
import pandas as pd
from api.models.endereco import EnderecoAnonimizado
from api.db import SessionLocal

endereco_campos = {
    'id': fields.Integer,
    'cep': fields.String,
    'rua': fields.String,
    'bairro': fields.String,
    'cidade': fields.String,
    'estado': fields.String,
    'pais': fields.String,
    'complemento': fields.String
}

class Endereco(Resource):
    @marshal_with(endereco_campos)
    def post(self):
        novo_endereco = request.get_json()
        df_endereco_anonimizado = pd.DataFrame([novo_endereco]).loc[:, ['id', 'cep', 'rua', 'bairro', 'cidade', 'estado', 'pais']]
        df_endereco_anonimizado['cep'] = df_endereco_anonimizado['cep'].map(Anonimizacao.hashear)
        df_endereco_anonimizado['rua'] = df_endereco_anonimizado['rua'].map(Anonimizacao.mascarar)
        df_endereco_anonimizado['bairro'] = df_endereco_anonimizado['bairro'].map(Anonimizacao.mascarar)
        df_endereco_anonimizado['cidade'] = df_endereco_anonimizado['cidade'].map(Anonimizacao.mascarar)
        endereco_anonimizado = EnderecoAnonimizado(**df_endereco_anonimizado.to_dict(orient='records')[0])
        
        with SessionLocal() as session:
            session.add(endereco_anonimizado)
            session.commit()
            session.refresh(endereco_anonimizado)
            print(session.query(EnderecoAnonimizado).all())

        return endereco_anonimizado, 201