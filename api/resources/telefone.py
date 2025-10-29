from flask_restful import Resource, marshal_with, fields
from flask import request
import pandas as pd
from api.utils.anonimizacao import Anonimizacao
from api.models.telefone import TelefoneAnonimizado
from api.db import SessionLocal

telefone_campos = {
    'id': fields.Integer,
    'num_telefone': fields.String,
    'id_cliente': fields.Integer,
}

class Telefone(Resource):
    @marshal_with(telefone_campos)
    def post(self):
        novo_telefone = request.get_json()
        df_telefone_anonimizado = pd.DataFrame([novo_telefone])
        df_telefone_anonimizado['num_telefone'] = df_telefone_anonimizado['num_telefone'].map(Anonimizacao.mascarar)

        telefone_anonimizado = TelefoneAnonimizado(**df_telefone_anonimizado.to_dict(orient='records')[0])

        with SessionLocal() as session:
            session.add(telefone_anonimizado)
            session.commit()
            session.refresh(telefone_anonimizado)
            print(session.query(TelefoneAnonimizado).all())

        return telefone_anonimizado, 201