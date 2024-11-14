from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23)

print("Rilevazione oggetto.....")
sensor.wait_for_in_range()
print("Oggetto rilevato nel range d'azione!!!!")
