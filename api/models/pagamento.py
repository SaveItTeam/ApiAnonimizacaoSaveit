from api.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

class PagamentoAnonimizado(Base):
    __tablename__ = 'pagamento_anonimizado'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    status: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    dt_criacao: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    dt_validade: Mapped[str] = mapped_column(sa.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"PagamentoAnonimizado(id={self.id!r}, status={self.status!r}, dt_criacao={self.dt_criacao!r}, dt_validade={self.dt_validade!r})"