from fastapi import APIRouter
from app.db import SessionLocal
from app.models.alert import Alert

router = APIRouter()

@router.get("/alerts")
def get_alerts():
    db = SessionLocal()
    return db.query(Alert).filter(Alert.is_active == True).all()
