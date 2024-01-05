import RPi.GPIO as GPIO
import ADC0834
from time import sleep
DT = .1
RLED = 23
dc = 0

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(RLED, GPIO.OUT)

myPWM = GPIO.PWM(RLED, 1000)
myPWM.start(dc)

try:
    while True:
        potValue = ADC0834.getResult(0)
        dc = (100/255) * potValue           # potValue / 2.5
        if dc > 99:
            dc = 99
        myPWM.ChangeDutyCycle(dc)
        print(potValue, dc)
        sleep(DT)

except KeyboardInterrupt:
    myPWM.stop()
    GPIO.cleanup()
    print('GPIO Good to Go.')