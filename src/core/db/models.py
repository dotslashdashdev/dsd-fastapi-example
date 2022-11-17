from sqlalchemy import Boolean, Column, DateTime, Integer, String

from core.db.base import Base
from core.utils import utc_now


class Users(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    email = Column(String(100), unique=True)
    status = Column(String(20), nullable=False, default="activation")
    nickname = Column(String(50), nullable=False)
    join_datetime = Column(DateTime, nullable=False, default=utc_now)
    leave_datetime = Column(DateTime, nullable=True)
