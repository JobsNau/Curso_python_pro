from datetime import datetime
import pytz

Bogota=pytz.timezone("America/Bogota")
Bogota_date=datetime.now(Bogota)
print("Bogota: ", Bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

Mexico=pytz.timezone("America/Mexico_City")
Mexico_date=datetime.now(Mexico)
print("Mexico: ", Mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))