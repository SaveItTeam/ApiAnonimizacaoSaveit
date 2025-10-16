from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class PlanoAnonimizado(Base):
    __tablename__ = 'plano_anonimizado'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    preco: Mapped[float] = mapped_column(sa.Float, nullable=False)
    descricao: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    id_pagamento: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('pagamento_anonimizado.id'), nullable=False)

    def __repr__(self):
        return f"PlanoAnonimizado(id={self.id!r}, cnpj={self.preco!r}, descricao={self.descricao!r}, id_pagamento={self.id_pagamento!r})"