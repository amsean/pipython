
import RPi.GPIO as GPIO
from time import sleep 

LED = 17
INPUT = 21
ON = False
OFF = True
DELAY = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        readVal = GPIO.input(INPUT)
        print(readVal)
        sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()


