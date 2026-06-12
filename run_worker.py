import time
from app.db import SessionLocal
from app.models.site import Site
from app.services.monitoring_service import check_sites

while True:
    db = SessionLocal()
    sites = db.query(Site).filter(Site.is_active == True).all()
    check_sites(db, sites)
    db.close()
    time.sleep(30)
