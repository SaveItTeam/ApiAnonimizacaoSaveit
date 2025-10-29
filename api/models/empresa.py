from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class EmpresaAnonimizada(Base):
    __tablename__ = 'empresa_anonimizada'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    procura: Mapped[str] = mapped_column(sa.Text, nullable=False)
    cod_empresa: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    id_cliente: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('cliente_anonimizado.id'), nullable=False)

    def __repr__(self) -> str:
        return f"EmpresaAnonimizada(id={self.id!r}, procura={self.procura!r}, id_={self.id_cliente!r})"