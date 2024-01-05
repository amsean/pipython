
import RPi.GPIO as GPIO
from time import sleep 

LED = 17
BUT = 21
ON = False
OFF = True
DELAY = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUT, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print('-------------------------------')
print('Folks, Lets Get Started:')
print('Press CTRL-C to Quit!')
print('-------------------------------')

try:
    while True:
        readVal = GPIO.input(BUT)
        if readVal == 1:
            GPIO.output(LED, OFF)
        if readVal == 0:
            GPIO.output(LED, ON)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('Thats all Folks!')
            
