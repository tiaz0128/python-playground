from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, CHAR, Float, TIMESTAMP

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class HistoryMst(Base):
    __tablename__ = "clo_history_mst"

    his_id = Column(CHAR(128), primary_key=True)

    group_id = Column(CHAR(128), nullable=False)
    key_id = Column(CHAR(128), nullable=False)

    ruleset_id = Column(CHAR(128))

    schedule_yn = Column(CHAR(32))
    status = Column(CHAR(128))
    error = Column(CHAR(128))
    instance_id = Column(CHAR(128))

    high = Column(Integer)
    medium = Column(Integer)
    low = Column(Integer)
    good = Column(Integer)
    na = Column(Integer)

    total_score = Column(Float)

    del_yn = Column(CHAR(2))

    ins_dt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.UTC_TIMESTAMP()
    )
    ins_user = Column(String(128), nullable=False)

    upd_dt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.UTC_TIMESTAMP()
    )
    upd_user = Column(String(128), nullable=False)
