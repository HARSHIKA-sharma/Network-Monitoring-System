from datetime import datetime

from app.db import SessionLocal
from app.models.site import Site
from app.models.status_log import StatusLog
from app.models.alert import Alert
from app.utils.ping import ping_host


def get_sites_status():
    """
    Used by the dashboard (status API) to get live UP/DOWN status
    for Router / BSNL / Jio for each site.
    """
    db = SessionLocal()
    sites = db.query(Site).all()

    data = []

    for s in sites:
        # latency or None
        router_lat = ping_host(s.router_ip)
        bsnl_lat = ping_host(s.bsnl_ip) if s.bsnl_ip else None
        jio_lat = ping_host(s.jio_ip) if s.jio_ip else None

        def status_from_latency(lat, has_ip):
            if not has_ip:
                return "NA"
            return "UP" if lat else "DOWN"

        data.append({
            "plant_code": s.plant_code,
            "location": s.location_name,
            "router": status_from_latency(router_lat, bool(s.router_ip)),
            "bsnl": status_from_latency(bsnl_lat, bool(s.bsnl_ip)),
            "jio": status_from_latency(jio_lat, bool(s.jio_ip)),
        })

    db.close()
    return data


def check_sites(db, sites):
    """
    Optional: used by run_worker.py to log status & create alerts.
    For now we only check router_ip and record one log per site.
    """
    for s in sites:
        latency = ping_host(s.router_ip)
        status = "online" if latency else "offline"

        log = StatusLog(
            site_id=s.id,
            status=status,
            latency=latency,
        )
        db.add(log)

        if status == "offline":
            alert = Alert(
                site_id=s.id,
                message=f"{s.location_name} is DOWN",
            )
            db.add(alert)

    db.commit()

