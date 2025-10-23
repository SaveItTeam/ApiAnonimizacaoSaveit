from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class FuncionarioAnonimizado(Base):
    __tablename__ = 'funcionario_anonimizado'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    cpf: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    rg: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    dt_nascimento: Mapped[datetime] = mapped_column(sa.Date, nullable=False)
    email: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    email_dominio: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    senha: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    cargo: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    dt_contratacao: Mapped[datetime] = mapped_column(sa.Date, nullable=False)
    telefone_pessoal: Mapped[str] = mapped_column(sa.String(20), nullable=False)
    telefone_trabalho: Mapped[str] = mapped_column(sa.String(20), nullable=False)
    experiencia: Mapped[str] = mapped_column(sa.Text, nullable=False)
    id_empresa: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('empresa_anonimizada.id'), nullable=False)
    id_industria: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('industria_anonimizada.id'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(sa.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"FuncionarioAnonimizado(id={self.id!r}, nome={self.nome!r}, cpf={self.cpf!r}, rg={self.rg!r}, dt_nascimento={self.dt_nascimento!r}, email={self.email!r}, senha={self.senha!r}, cargo={self.cargo!r}, dt_contratacao={self.dt_contratacao!r}, telefone_pessoal={self.telefone_pessoal!r}, telefone_trabalho={self.telefone_trabalho!r}, experiencia={self.experiencia!r}, id_empresa={self.id_empresa!r}, id_industria={self.id_industria!r}, is_admin={self.is_admin!r})"