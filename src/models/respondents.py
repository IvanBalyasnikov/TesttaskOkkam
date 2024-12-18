from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class RespondentsOrm(Base):
    __tablename__ = "respodents"

    id:Mapped[int] = mapped_column(primary_key=True)
    Date:Mapped[str] = mapped_column(name = "date")
    respondent:Mapped[int] = mapped_column(unique=False)
    Sex:Mapped[int] = mapped_column(name="sex")
    Age:Mapped[int] = mapped_column(name="age")
    Weight:Mapped[float] = mapped_column(name="weight")
    