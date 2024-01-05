import RPi.GPIO as GPIO
from time import sleep

DT = 0.1
BUT1 = 22
BUT2 = 27
but1State = 1
but1StatePre = 1
but2State = 1
but2StatePre = 1
LED = 26
dc = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
myPWM = GPIO.PWM(LED, 100)
myPWM.start(dc)

try:
    while True:
        but1State = GPIO.input(BUT1)
        but2State = GPIO.input(BUT2)
        if but1StatePre != but1State:
            if but1State == 1:
                dc = dc - 10
                print('Dim Event')
            but1StatePre = but1State
        if but2StatePre != but2State:
            if but2State == 1:
                dc = dc + 10
                print('Bright Event')
            but2StatePre = but2State
        if dc > 100:
            dc = 100
        if dc < 0:
            dc = 0
        myPWM.ChangeDutyCycle(dc)
        sleep(DT)

except KeyboardInterrupt:
        myPWM.stop()
        GPIO.cleanup()
        print('\r\nGPIO Good to GO')

