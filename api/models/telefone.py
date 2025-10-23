from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class TelefoneAnonimizado(Base):
    __tablename__ = 'telefone_anonimizado'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    num_telefone: Mapped[str] = mapped_column(sa.String(20), nullable=False)
    id_cliente: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('cliente_anonimizado.id'), nullable=False)

    def __repr__(self) -> str:
        return f"TelefoneAnonimizado(id={self.id!r}, numero={self.num_telefone!r}, id_cliente={self.id_cliente!r})"