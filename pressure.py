import RPi.GPIO as GPIO
import time
def pressure():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.IN)
    if not GPIO.input(25):
        return 0
    else:
        return 1
def buttom1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24,GPIO.IN,GPIO.PUD_UP)
    while(1):
        time.sleep(0.05)
        if(GPIO.input(24)==0):
            return 1
        