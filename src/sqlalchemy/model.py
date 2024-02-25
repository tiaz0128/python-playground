from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = "test"
    __table_args__ = {"schema": "test"}

    id: Mapped[int] = mapped_column(primary_key=True)
    desc: Mapped[str] = mapped_column(String(30))


class Test2(Base):
    __tablename__ = "test"

    id: Mapped[int] = mapped_column(primary_key=True)
    desc: Mapped[str] = mapped_column(String(30))
