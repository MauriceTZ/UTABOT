import serial
import time
import threading
import glm

s = serial.Serial("COM6", 115200)
s.timeout = 0.2


def salida(pin: int):
    s.write(f"attachServo({pin});".encode())
    # time.sleep(0.1)
    # print(s.readline().decode(), end="")


def write(pin: int, angle: int):
    s.write(f"setAngle({pin}, {angle});\n".encode())
    # time.sleep(0.1)
    # print(s.readline().decode(), end="")


def t():
    while True:
        print(s.read_all().decode(), end="")
        # time.sleep(0.01)


threading.Thread(target=t).start()


class Servo:
    def __init__(self, pin, sentido=1) -> None:
        self.pin = pin
        self._angulo = 90
        self.sentido = sentido
        salida(self.pin)
        time.sleep(0.1)
        write(self.pin, self._angulo)
        time.sleep(0.1)

    @property
    def angulo(self):
        return self._angulo

    @angulo.setter
    def angulo(self, a):
        self._angulo = glm.clamp(a, 0, 180)
        if self.sentido:
            write(self.pin, self._angulo)
        else:
            write(self.pin, 180 - self._angulo)


class Pierna:
    def __init__(self, cadera, rodilla, tobillo, pie,
                 sentido_cadera=1, sentido_rodilla=1, sentido_tobillo=1, sentido_pie=1) -> None:
        self.cadera = Servo(cadera, sentido_cadera)
        self.rodilla = Servo(rodilla, sentido_rodilla)
        self.tobillo = Servo(tobillo, sentido_tobillo)
        self.pie = Servo(pie, sentido_pie)


class JuanBot:
    def __init__(self) -> None:
        self.pierna_izq = Pierna(32, 33, 27, 14,
                                 1,  0,  0,  0)
        self.pierna_der = Pierna(12, 4, 16, 2,
                                 0,  1,  1,  1)
        print(f"{self.__class__.__name__} Inicializado.")


juanbot = JuanBot()
# while True:
#     expresion = input().split("=")
#     print(exec(f"juanbot.{expresion[0]}.angulo={expresion[1]}"))
    # a = int(input("angulo: "))
    # juanbot.pierna_der.tobillo.angulo = a
    # juanbot.pierna_izq.tobillo.angulo = a


juanbot.pierna_der.cadera.angulo = 90+45-15
juanbot.pierna_izq.cadera.angulo = 90+45-15

juanbot.pierna_der.rodilla.angulo = 90-45*2+15-8
juanbot.pierna_izq.rodilla.angulo = 90-45*2+15

juanbot.pierna_der.tobillo.angulo = 90+45+15
juanbot.pierna_izq.tobillo.angulo = 90+45+15

# offset de 8



# time.sleep(1)
# for x in range(90-45*2, 90-45*2+15, 1):
#     print(f"angulo: {x}")
#     juanbot.pierna_der.rodilla.angulo = x
#     time.sleep(1)

# time.sleep(1)
# for x in range(90-45*2, 90-45*2+15, 1):
#     print(f"angulo: {x}")
#     juanbot.pierna_der.tobillo.angulo = x
#     time.sleep(1)

# juanbot.pierna_der.pie.angulo = 110