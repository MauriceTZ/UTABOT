import serial
import time
import threading

s = serial.Serial("/dev/ttyUSB0", 115200)
s.timeout = 0.3


def salida(pin: int):
    s.write(f"attachServo({pin});".encode())
    # print(s.readline().decode(), end="")


def write(pin: int, angle: int):
    s.write(f"setAngle({pin}, {angle});\n".encode())
    # print(s.readline().decode(), end="")


def t():
    while True:
        print(s.read_all().decode(), end="")

threading.Thread(target=t).start()

cadera = 33
pierna = 25
rodilla = 12
tobillo = 27
salida(cadera)
salida(pierna)
salida(rodilla)
salida(tobillo)
time.sleep(1)

write(cadera, 40)
time.sleep(2)
write(pierna, 50)
time.sleep(2)
write(rodilla, 120)
time.sleep(2)

time.sleep(2)
write(cadera, 90)
time.sleep(2)
write(pierna, 90)
time.sleep(2)
write(rodilla, 90)
time.sleep(2)

print("OK")



# rod_izq = 32
# pierna_izq = 33
# tobillo_izq = 25

# salida(rod_izq)
# salida(pierna_izq)
# salida(tobillo_izq)

# for _ in range(3):
#     for x in range(10, 150):
#         write(pierna_izq, x)
#         write(rod_izq, 150-x)
#         time.sleep(0.01)

#     for x in range(150, 10, -1):
#         write(pierna_izq, x)
#         write(rod_izq, 150-x)
#         time.sleep(0.01)

# for _ in range(3):
#     write(rod_izq, 170)
#     write(pierna_izq, 10)
#     time.sleep(1)
    
#     write(rod_izq, 90)
#     write(pierna_izq, 90)
#     time.sleep(1)




# brazo_izq = 32
# hombro_izq = 33

# salida(brazo_izq)
# salida(hombro_izq)

# for _ in range(3):
#     write(hombro_izq, 10)
#     time.sleep(2)
#     write(brazo_izq, 50)
#     time.sleep(2)
#     write(hombro_izq, 170)
#     time.sleep(2)
#     write(brazo_izq, 130)
#     time.sleep(2)
#     write(brazo_izq, 90)
#     write(hombro_izq, 90)
#     time.sleep(2)

# while True:
#     for x in range(30, 140, 1):
#         write(pin, x)
#         time.sleep(0.01)
#     for x in range(140, 30, -1):
#         write(pin, x)
#         time.sleep(0.01)

