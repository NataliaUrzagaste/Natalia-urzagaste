import random
import time

print("sensor encendido")
def sensordemovimiento():
    inicio_time = time.time()
    while time.time() - inicio_time < 10.0:
        movimiento = random.randint(0.0, 10.0)
        if movimiento > 5.0:
            print("movimiento detectado")
            time.sleep(1)
        else:
            print("no hay movimiento")
            time.sleep(1)

sensordemovimiento()
print("sensor apagado")
time.sleep(20)

