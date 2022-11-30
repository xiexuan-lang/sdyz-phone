from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from time import sleep
pigpio_factory = PiGPIOFactory()
servo = Servo(23, pin_factory=pigpio_factory)
servo.value= -0.6
sleep(2)
servo.value =1

