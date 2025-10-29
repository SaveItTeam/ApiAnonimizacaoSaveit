from flask_restful import Resource, marshal_with, fields
from flask import request
import pandas as pd
from api.utils.anonimizacao import Anonimizacao
from api.models.funcionario import FuncionarioAnonimizado
from api.db import SessionLocal

funcionario_campos = {
    'id': fields.Integer,
    'nome': fields.String,
    'cpf': fields.String,
    'rg': fields.String,
    'genero': fields.String,
    'dt_nascimento': fields.String,
    'email': fields.String,
    'senha': fields.String,
    'cargo': fields.String,
    'dt_contratacao': fields.String,
    'telefone_pessoal': fields.String,
    'telefone_trabalho': fields.String,
    'experiencia': fields.String,
    'id_empresa': fields.Integer,
    'id_industria': fields.Integer,
    'is_admin': fields.Boolean
}

class Funcionario(Resource):
    @marshal_with(funcionario_campos)
    def post(self):
        novo_funcionario = request.get_json()
        df_funcionario_anonimizado = pd.DataFrame([novo_funcionario]).loc[:, ['id', 'nome', 'cpf', 'rg', 'dt_nascimento', 'email', 'senha', 'cargo', 'dt_contratacao', 'telefone_pessoal', 'telefone_trabalho', 'experiencia', 'id_empresa', 'id_industria']]
        df_funcionario_anonimizado['nome'] = df_funcionario_anonimizado['nome'].map(Anonimizacao.criptografar)
        df_funcionario_anonimizado['cpf'] = df_funcionario_anonimizado['cpf'].map(Anonimizacao.hashear)
        df_funcionario_anonimizado['rg'] = df_funcionario_anonimizado['rg'].map(Anonimizacao.hashear)
        df_funcionario_anonimizado['dt_nascimento'] = df_funcionario_anonimizado['dt_nascimento'].map(Anonimizacao.generalizar_data)
        df_funcionario_anonimizado['email_dominio'] = df_funcionario_anonimizado['email'].map(Anonimizacao.pegar_dominio)
        df_funcionario_anonimizado['email'] = df_funcionario_anonimizado['email'].map(Anonimizacao.hashear)
        df_funcionario_anonimizado['senha'] = df_funcionario_anonimizado['senha'].map(Anonimizacao.hashear)
        df_funcionario_anonimizado['cargo'] = df_funcionario_anonimizado['cargo'].map(Anonimizacao.generalizar_cargo)
        df_funcionario_anonimizado['dt_contratacao'] = df_funcionario_anonimizado['dt_contratacao'].map(Anonimizacao.generalizar_data)
        df_funcionario_anonimizado['telefone_pessoal'] = df_funcionario_anonimizado['telefone_pessoal'].map(Anonimizacao.mascarar)
        df_funcionario_anonimizado['telefone_trabalho'] = df_funcionario_anonimizado['telefone_trabalho'].map(Anonimizacao.mascarar)
        funcionario_anonimizado = FuncionarioAnonimizado(**df_funcionario_anonimizado.to_dict(orient='records')[0])

        with SessionLocal() as session:
            session.add(funcionario_anonimizado)
            session.commit()
            session.refresh(funcionario_anonimizado)
            print(session.query(FuncionarioAnonimizado).all())

        return funcionario_anonimizado, 201