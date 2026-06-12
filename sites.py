from fastapi import APIRouter
from app.db import SessionLocal
from app.models.site import Site

router = APIRouter()

@router.post("/sites")
def add_site(name: str, ip: str, location: str):
    db = SessionLocal()
    site = Site(name=name, ip_address=ip, location=location)
    db.add(site)
    db.commit()
    return {"message": "Site added"}

@router.get("/sites")
def list_sites():
    db = SessionLocal()
    return db.query(Site).all()
