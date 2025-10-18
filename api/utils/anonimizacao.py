import hashlib
from cryptography.fernet import Fernet
from datetime import datetime, date
import re

key = Fernet.generate_key()
f = Fernet(key)

class Anonimizacao:
    @staticmethod
    def hashear(valor: str) -> str:
        return hashlib.sha256(valor.encode()).hexdigest()

    @staticmethod
    def criptografar(valor: str) -> str:
        return f.encrypt(valor.encode()).decode()

    @staticmethod
    def descriptografar(criptografia: str) -> str:
        return f.decrypt(criptografia.encode()).decode()

    @staticmethod
    def mascarar(valor: str) -> str:
        return valor[0] + ''.join('*' if c.isalnum() else c for c in valor[1:-1]) + valor[-1]
    
    @staticmethod
    def pegar_dominio(email: str) -> str:
        return re.search(r'@([^.]+)\.', email).group(1)
    
    @staticmethod
    def generalizar_cargo(cargo: str) -> str:
        cargos = {
            "CEO": "Gestão",
            "Diretor": "Gestão",
            "Gerente": "Gestão",
            "Desenvolvedor": "Tecnologia",
            "Engenheiro de Software": "Tecnologia",
            "Estagiário": "Suporte",
            "Analista": "Suporte"
        }
        return cargos.get(cargo, 'Outro')
    
    @staticmethod
    def generalizar_data(data: str) -> datetime:
        data = datetime.strptime(data, '%Y-%m-%d')
        return date(data.year, data.month, 1)