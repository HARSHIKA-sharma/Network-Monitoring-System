from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db import Base

class StatusLog(Base):
    __tablename__ = "status_logs"

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey("sites.id"))
    status = Column(String)
    latency = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())

