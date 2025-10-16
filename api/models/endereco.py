from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class EnderecoAnonimizado(Base):
    __tablename__ = 'endereco_anonimizado'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    cep: Mapped[str] = mapped_column(sa.String(20), nullable=False)
    rua: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    bairro: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    cidade: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    estado: Mapped[str] = mapped_column(sa.String(10), nullable=False)
    pais: Mapped[str] = mapped_column(sa.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"EnderecoAnonimizado(id={self.id!r}, cep={self.cep!r}, rua={self.rua!r}, bairro={self.bairro!r}, cidade={self.cidade!r}, estado={self.estado!r}, pais={self.pais!r})"