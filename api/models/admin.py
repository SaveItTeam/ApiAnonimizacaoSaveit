from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class AdminAnonimizado(Base):
    __tablename__ = 'admin_anonimizado'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    nome_admin: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    email_dominio: Mapped[str] = mapped_column(sa.String(32), nullable=False)
    senha: Mapped[str] = mapped_column(sa.String(64), nullable=False)

    def __repr__(self) -> str:
        return f"AdminAnonimizado(id={self.id!r}, nome_admin={self.nome_admin!r}, email={self.email!r}, email_dominio={self.email_dominio!r}, senha={self.senha!r})"