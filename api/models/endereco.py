from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class EnderecoAnonimizado(Base):
    __tablename__ = 'endereco_anonimizado'
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    cep: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    cep_rua: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    cep_bairro: Mapped[str] = mapped_column(sa.String(128), nullable=False)
    cep_estado: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    cep_pais: Mapped[str] = mapped_column(sa.String(32), nullable=False)

    def __repr__(self) -> str:
        return f"EnderecoAnonimizado(id={self.id!r}, cep={self.cep!r}, rua={self.cep_rua!r}, bairro={self.cep_bairro!r}, estado={self.cep_estado!r}, pais={self.cep_pais!r})"