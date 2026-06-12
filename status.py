from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.services.monitoring_service import get_sites_status

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def dashboard(request: Request):
    data = get_sites_status()

    total_sites = len(data)
    router_up = sum(1 for r in data if r["router"] == "UP")
    router_down = sum(1 for r in data if r["router"] == "DOWN")
    bsnl_up = sum(1 for r in data if r["bsnl"] == "UP")
    jio_up = sum(1 for r in data if r["jio"] == "UP")

    context = {
        "request": request,
        "data": data,
        "total_sites": total_sites,
        "router_up": router_up,
        "router_down": router_down,
        "bsnl_up": bsnl_up,
        "jio_up": jio_up,
        "last_refreshed": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    }

    return templates.TemplateResponse("dashboard.html", context)