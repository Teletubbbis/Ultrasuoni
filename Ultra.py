import RPi.GPIO as GPIO
import time

# Configura i pin GPIO
GPIO.setmode(GPIO.BCM)
TRIG = 17     # Pin TRIG collegato al pin GPIO 17
ECHO = 29     # Pin ECHO collegato al pin GPIO 29

# Configurazione dei pin di input/output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def misura_distanza():
    # Attiva il trigger per 10 microsecondi
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Calcola il tempo di andata e ritorno dell'eco
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()

    # Calcolo della distanza
    tempo_trascorso = end - start
    distanza = (tempo_trascorso * 34300) / 2  # Velocità del suono 34300 cm/s
    return distanza

try:
    while True:
        distanza = misura_distanza()
        print(f"Distanza misurata: {distanza:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Misurazione interrotta dall'utente")

finally:
    GPIO.cleanup()
