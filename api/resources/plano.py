from flask_restful import Resource, marshal_with, fields
from flask import request
import pandas as pd
from api.db import SessionLocal
from api.models.plano import PlanoAnonimizado

plano_campos = {
    'id': fields.Integer,
    'preco': fields.Float,
    'descricao': fields.String,
}

class Plano(Resource):
    @marshal_with(plano_campos)
    def post(self):
        novo_plano = request.get_json()
        df_plano_anonimizado = pd.DataFrame([novo_plano])
        plano_anonimizado = PlanoAnonimizado(**df_plano_anonimizado.to_dict(orient='records')[0])

        with SessionLocal() as session:
            session.add(plano_anonimizado)
            session.commit()
            session.refresh(plano_anonimizado)
            print(session.query(PlanoAnonimizado).all())

        return plano_anonimizado, 201