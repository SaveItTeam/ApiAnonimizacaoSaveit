from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class IndustriaAnonimizada(Base):
    __tablename__ = "industria_anonimizada"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    vende: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    id_plano: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('plano_anonimizado.id'), nullable=False)
    id_pagamento: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('pagamento_anonimizado.id'), nullable=False)
    id_cliente: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('cliente_anonimizado.id'), nullable=False)

    def __repr__(self) -> str:
        return f"IndustriaAnonimizada(id={self.id!r}, vende={self.vende!r}, id_plano={self.id_plano!r}, id_pagamento={self.id_pagamento!r}, id_cliente={self.id_cliente!r})"