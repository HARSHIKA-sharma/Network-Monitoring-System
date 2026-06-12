from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db import Base

class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)

    plant_code = Column(String)
    location_name = Column(String)

    router_ip = Column(String)
    bsnl_ip = Column(String)
    jio_ip = Column(String)

    reachable_ip = Column(String)   # ✅ ADD THIS LINE

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())



