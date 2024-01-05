import RPi.GPIO as GPIO
import ADC0834
from time import sleep

GPIO.setmode(GPIO.BCM)
ADC0834.setup()

try:
    while True:
        analogValue = ADC0834.getResult(0)
        print(analogValue)
        sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()