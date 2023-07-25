from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from time import sleep

factory = PiGPIOFactory()
servo = AngularServo(18, min_angle=-60, max_angle = 90, min_pulse_width=0.0009, max_pulse_width=0.0021, pin_factory = factory)
angle_base = 0

while (True):
    angle = int(input("Angle: "))

    angle_base = angle
    servo.angle = angle_base

    print(angle, angle_base)