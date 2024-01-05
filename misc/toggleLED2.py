
import RPi.GPIO as GPIO
from time import sleep 

LED = 17
BUT = 21
ON = False
OFF = True
DELAY = .1

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUT, GPIO.IN, pull_up_down = GPIO.PUD_UP)

LEDState = 0
BUTState = 1
BUTStatePre = 1

try:
    while True:
        BUTState = GPIO.input(BUT)
        print(BUTState)
        if BUTState != BUTStatePre:
            if BUTState == 0:
                LEDState = not LEDState
            BUTStatePre = BUTState
        GPIO.output(LED, LEDState)
        sleep(DELAY)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('Thats all Folks!')
            
