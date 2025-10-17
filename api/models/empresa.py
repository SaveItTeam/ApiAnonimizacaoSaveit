from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class EmpresaAnonimizada(Base):
    __tablename__ = 'empresa_anonimizada'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    id_funcionario: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('funcionario_anonimizado.id'), nullable=False)
    id_cliente: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('cliente_anonimizado.id'), nullable=False)
    procura: Mapped[str] = mapped_column(sa.Text, nullable=False)
    id_plano: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('plano_anonimizado.id'), nullable=False)

    def __repr__(self) -> str:
        return f"EmpresaAnonimizada(id={self.id!r}, id_funcionario={self.id_funcionario!r}, id_cliente={self.id_cliente!r}, procura={self.procura!r}, id_plano={self.id_plano!r})"