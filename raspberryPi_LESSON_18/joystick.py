import RPi.GPIO as GPIO
import ADC0834
from time import sleep

BUT = 21
GPIO.setmode(GPIO.BCM)
ADC0834.setup()

GPIO.setup(BUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        analogValX = ADC0834.getResult(0)
        sleep(.1)
        analogValY = ADC0834.getResult(1)
        butState = GPIO.input(BUT)
        print('X = ', analogValX, 'Y = ', analogValY, 'Button: ', butState)
        
        sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go.')