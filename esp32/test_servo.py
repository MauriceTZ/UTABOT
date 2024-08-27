import serial
import time
import threading

s = serial.Serial("/dev/ttyUSB0", 115200)
s.timeout = 0.3


def salida(pin: int):
    s.write(f"attachServo({pin});".encode())


def write(pin: int, angle: int):
    s.write(f"setAngle({pin}, {angle});\n".encode())


def t():
    while True:
        print(s.read_all().decode(), end="")

#threading.Thread(target=t).start()

izq_cadera=32
izq_rodilla=33
izq_tobillo=27
izq_pie=14

salida(izq_cadera)
salida(izq_rodilla)
salida(izq_tobillo)
salida(izq_pie)

write(izq_cadera,160)
write(izq_rodilla,140)
write(izq_tobillo,90)
write(izq_pie,90)

time.sleep(2)

write(izq_cadera,90)
write(izq_rodilla,90)
write(izq_tobillo,90)
write(izq_pie,90)



print("OK")
