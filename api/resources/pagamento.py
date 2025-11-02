from flask_restful import Resource, marshal_with, fields
from flask import request
import pandas as pd
from api.utils.anonimizacao import Anonimizacao
from api.models.pagamento import PagamentoAnonimizado
from api.db import SessionLocal

pagamento_campos = {
    'id': fields.Integer,
    'status': fields.String,
    'dt_criacao': fields.String,
    'dt_validade': fields.String,
    'forma_pagamento': fields.String
}

class Pagamento(Resource):
    @marshal_with(pagamento_campos)
    def post(self):
        novo_pagamento = request.get_json()
        df_pagamento_anonimizado = pd.DataFrame([novo_pagamento])
        df_pagamento_anonimizado['dt_criacao'] = df_pagamento_anonimizado['dt_criacao'].map(Anonimizacao.generalizar_data)
        df_pagamento_anonimizado['dt_validade'] = df_pagamento_anonimizado['dt_validade'].map(Anonimizacao.generalizar_data)
        pagamento_anonimizado = PagamentoAnonimizado(**df_pagamento_anonimizado.to_dict(orient='records')[0])

        with SessionLocal() as session:
            session.add(pagamento_anonimizado)
            session.commit()
            session.refresh(pagamento_anonimizado)
            print(session.query(PagamentoAnonimizado).all())

        return pagamento_anonimizado, 201