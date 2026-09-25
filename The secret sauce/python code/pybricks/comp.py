from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import UARTDevice

hub = PrimeHub()
rp2040 = UARTDevice(Port.F, baudrate=115200)
usf = UltrasonicSensor(Port.E)
usr = UltrasonicSensor(Port.A)
usl = UltrasonicSensor(Port.B)
power = Motor(Port.C)
steer = Motor(Port.D)

usf.lights.on(100)
usl.lights.on(100)
usr.lights.on(100)
rp2040.write('go')

while True:
    print('started')
    power.dc(65)
    steer.track_target(0)
    if usf.distance() < 575:
        print('wall seen')
        if usl.distance() > usr.distance():
            print('went left')
            steer.run_target(-35)
            wait(700)
            steer.run_target(0)
            wait(1)
            steer.run_target(45)
        else:
            if usl.distance() < usr.distance():
                print('went right')
                steer.run_target(35)
                wait(700)
                steer.run_target(0)
                wait(1)
                steer.run_target(-45)
                