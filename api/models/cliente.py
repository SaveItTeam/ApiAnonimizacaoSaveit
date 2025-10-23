from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class ClienteAnonimizado(Base):
    __tablename__ = 'cliente_anonimizado'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    email_dominio: Mapped[str] = mapped_column(sa.String(32), nullable=False)
    senha: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    tipo: Mapped[int] = mapped_column(sa.Integer, nullable=False)
    tipo_venda: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    id_endereco: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('endereco_anonimizado.id'), nullable=False)
    cnpj: Mapped[str] = mapped_column(sa.String(64), nullable=False)

    def __repr__(self) -> str:
        return f"ClienteAnonimizado(id={self.id!r}, nome={self.nome!r}, email={self.email!r}, email_dominio={self.email_dominio!r}, senha={self.senha!r}, tipo={self.tipo!r}'), tipo_venda={self.tipo_venda!r}, id_endereco={self.id_endereco!r}, cnpj={self.cnpj!r})"