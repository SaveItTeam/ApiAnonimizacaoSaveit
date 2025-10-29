from flask_restful import Resource, marshal_with, fields
from flask import request
import pandas as pd
from api.models.industria import IndustriaAnonimizada
from api.db import SessionLocal
from api.utils.anonimizacao import Anonimizacao

industria_campos = {
    'id': fields.Integer,
    'vende': fields.String,
    'id_plano': fields.Integer,
    'cod_industria': fields.String,
    'id_pagamento': fields.Integer,
    'id_cliente': fields.Integer
}

class Industria(Resource):
    @marshal_with(industria_campos)
    def post(self):
        nova_industria = request.get_json()
        df_industria_anonimizada = pd.DataFrame([nova_industria])
        df_industria_anonimizada['cod_industria'] = df_industria_anonimizada['cod_industria'].map(Anonimizacao.hashear)
        industria_anonimizada = IndustriaAnonimizada(**df_industria_anonimizada.to_dict(orient='records')[0])

        with SessionLocal() as session:
            session.add(industria_anonimizada)
            session.commit()
            session.refresh(industria_anonimizada)
            print(session.query(IndustriaAnonimizada).all())

        return industria_anonimizada, 201