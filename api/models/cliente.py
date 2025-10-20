from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class ClienteAnonimizado(Base):
    __tablename__ = 'cliente_anonimizado'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    cnpj: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    nome: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    email_dominio: Mapped[str] = mapped_column(sa.String(32), nullable=False)
    senha: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    telefone: Mapped[str] = mapped_column(sa.String(16),nullable=False)
    tipo_venda: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    id_empresa: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('empresa_anonimizada.id'), nullable=False)
    id_endereco: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('endereco_anonimizado.id'), nullable=False)
    id_industria: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('industria_anonimizada.id'), nullable=False)

    def __repr__(self) -> str:
        return f"ClienteAnonimizado(id={self.id!r}, cnpj={self.cnpj!r}, nome={self.nome!r}, email={self.email!r}, telefone={self.telefone!r}'), tipo_venda={self.tipo_venda!r}, id_empresa={self.id_empresa!r}, id_endereco={self.id_endereco!r}, id_industria={self.id_industria!r})"