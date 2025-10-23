from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class PlanoAnonimizado(Base):
    __tablename__ = 'plano_anonimizado'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    preco: Mapped[float] = mapped_column(sa.Float, nullable=False)
    descricao: Mapped[str] = mapped_column(sa.Text, nullable=False)

    def __repr__(self):
        return f"PlanoAnonimizado(id={self.id!r}, cnpj={self.preco!r}, descricao={self.descricao!r})"