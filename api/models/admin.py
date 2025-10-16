from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class AdminAnonimizado(Base):
    __tablename__ = 'admin_anonimizado'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    cargo: Mapped[str] = mapped_column(sa.Text, nullable=False)
    nome_empresa: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    nome_admin: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    senha: Mapped[str] = mapped_column(sa.String(128), nullable=False)

    def __repr__(self) -> str:
        return f"AdminAnonimizado(id={self.id!r}, cargo={self.cargo!r}, nome_empresa={self.nome_empresa!r}, nome_admin={self.nome_admin!r}, senha={self.senha!r})"