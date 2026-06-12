from app.db import SessionLocal, engine, Base
from app.models.site import Site

# Create tables according to current models
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ----- CLEAR OLD DATA TO AVOID DUPLICATES -----
db.query(Site).delete()
db.commit()

# ----- INSERT ALL SITES (mentor list) -----
sites = [
    Site(plant_code="1029", location_name="Allahabad AFS",
         router_ip="10.40.33.1", bsnl_ip="172.31.142.5", jio_ip=None),

    Site(plant_code="1473", location_name="Allahabad BP",
         router_ip="10.40.34.1", bsnl_ip="172.31.142.1", jio_ip="172.24.198.86"),

    Site(plant_code="5578", location_name="Allahabad CFA",
         router_ip="10.40.38.1", bsnl_ip=None, jio_ip="172.24.199.202"),

    Site(plant_code="1401", location_name="Allahabad DO",
         router_ip="10.40.32.1", bsnl_ip="172.31.141.249", jio_ip="172.24.198.90"),

    Site(plant_code="1449", location_name="Ambabai Depot",
         router_ip="10.38.96.1", bsnl_ip="172.31.142.13", jio_ip="172.24.200.30"),

    Site(plant_code="1442", location_name="Baitalpur Depot",
         router_ip="10.40.128.1", bsnl_ip="172.31.143.249", jio_ip="172.24.200.34"),

    Site(plant_code="1022", location_name="Fursatganj AFS",
         router_ip="10.38.224.1", bsnl_ip="172.31.143.237", jio_ip="172.24.200.50"),

    Site(plant_code="1456", location_name="Gonda Depot",
         router_ip="10.38.128.1", bsnl_ip="172.31.142.17", jio_ip="172.24.200.42"),

    Site(plant_code="1025", location_name="Gorakhpur AFS",
         router_ip="10.38.193.1", bsnl_ip="172.31.142.25", jio_ip=None),

    Site(plant_code="1470", location_name="Gorakhpur BP",
         router_ip="10.38.192.1", bsnl_ip="172.31.174.69", jio_ip="172.24.199.78"),

    Site(plant_code="1026", location_name="Kanpur AFS",
         router_ip="10.38.64.1", bsnl_ip="172.31.174.113", jio_ip=None),

    Site(plant_code="1474", location_name="Kanpur BP",
         router_ip="10.38.65.1", bsnl_ip="172.31.142.29", jio_ip="172.24.198.178"),

    Site(plant_code="5577", location_name="Kanpur CFA",
         router_ip="10.38.70.1", bsnl_ip="172.31.143.241", jio_ip="172.24.199.198"),

    Site(plant_code="1407", location_name="Kanpur DO",
         router_ip="10.38.72.1", bsnl_ip="172.31.247.89", jio_ip="172.24.198.134"),

    Site(plant_code="1423", location_name="Kanpur Marketing Terminal",
         router_ip="10.38.66.1", bsnl_ip="172.31.173.229", jio_ip="172.24.198.110"),

    Site(plant_code="1031", location_name="Lucknow AFS",
         router_ip="10.38.44.1", bsnl_ip="172.31.142.41", jio_ip=None),

    Site(plant_code="1486", location_name="Lucknow BP (Amousi BP)",
         router_ip="10.38.37.1", bsnl_ip="172.31.175.101", jio_ip="172.24.198.186"),

    Site(plant_code="1426", location_name="Lucknow Marketing Terminal (Amousi Marketing Terminal)",
         router_ip="10.38.38.1", bsnl_ip="172.31.175.49", jio_ip="172.24.198.190"),

    Site(plant_code="1400", location_name="Uttar Pradesh SO 1",
         router_ip="10.38.36.1", bsnl_ip="172.31.173.233", jio_ip="172.24.198.30"),

    Site(plant_code="1424", location_name="Mughalsarai Marketing Terminal",
         router_ip="10.40.64.1", bsnl_ip="172.31.142.45", jio_ip="172.24.198.194"),

    Site(plant_code="1403", location_name="New Lucknow DO",
         router_ip="10.38.39.1", bsnl_ip="172.31.247.29", jio_ip="172.24.198.114"),

    Site(plant_code="1422", location_name="New-Allahabad Marketing Terminal",
         router_ip="10.40.35.1", bsnl_ip="172.31.175.197", jio_ip="172.24.198.198"),

    Site(plant_code="1471", location_name="TRISHUNDI BOTTLING PLANT",
         router_ip="10.38.160.1", bsnl_ip="172.31.141.41", jio_ip="172.24.198.222"),

    Site(plant_code="1030", location_name="Varanasi AFS",
         router_ip="10.40.97.1", bsnl_ip="172.31.142.53", jio_ip="172.24.200.66"),

    Site(plant_code="1482", location_name="Varanasi BP",
         router_ip="10.40.96.1", bsnl_ip="172.31.142.49", jio_ip="172.24.198.126"),

    Site(plant_code="1029", location_name="Allahabad AFS Civil Base",
         router_ip="10.40.36.1", bsnl_ip="172.31.174.149", jio_ip=None),

    Site(plant_code="1417", location_name="Varanasi Indane DO",
         router_ip="10.40.99.1", bsnl_ip="172.31.174.189", jio_ip="172.24.198.246"),

    Site(plant_code="1432", location_name="Mirzapur Terminal",
         router_ip="10.40.100.1", bsnl_ip=None, jio_ip="172.24.198.2"),

    Site(plant_code="1481", location_name="Gorakhpur CBG Plant",
         router_ip="10.38.196.1", bsnl_ip=None, jio_ip="172.24.194.230"),

    Site(plant_code="1406/1415", location_name="New Gorakhpur DO/IDO",
         router_ip="10.38.197.1", bsnl_ip="172.31.142.21", jio_ip="172.24.201.174"),
    Site(
    plant_code="GOOGLE",
    location_name="Google Public DNS",
    router_ip="8.8.8.8",   # Google DNS
    bsnl_ip=None,
    jio_ip=None
),Site(
    plant_code="GOOGLE",
    location_name="Google Public DNS",
    router_ip="8.8.8.8",   # Google DNS
    bsnl_ip=None,
    jio_ip=None
),

]

db.add_all(sites)
db.commit()
db.close()

print("Sites inserted successfully")