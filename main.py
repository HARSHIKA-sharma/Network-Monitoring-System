from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.db import Base, engine, SessionLocal
from app.models.site import Site
from app.routers import sites, status, alerts

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.include_router(sites.router)
app.include_router(status.router)
app.include_router(alerts.router)

@app.get("/")
def dashboard(request: Request):
    db = SessionLocal()
    sites = db.query(Site).all()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "sites": sites
    })
