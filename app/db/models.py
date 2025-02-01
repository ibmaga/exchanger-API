from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class UserInDB(Base):
    __tablename__ = 'users'

    # id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(primary_key=True, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

