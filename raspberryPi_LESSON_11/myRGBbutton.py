import RPi.GPIO as GPIO
from time import sleep
DT = 0.1
RLED = 26
GLED = 19
BLED = 13
RBUT = 22
GBUT = 27
BBUT = 17
rButState = 1
rButStatePre = 1
gButState = 1
gButStatePre = 1
bButState = 1
bButStatePre = 1
rLedState = 1
gLedState = 1
bLedState = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(RLED, GPIO.OUT)
GPIO.setup(GLED, GPIO.OUT)
GPIO.setup(BLED, GPIO.OUT)
GPIO.setup(RBUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GBUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BBUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        rButState =  GPIO.input(RBUT)
        gButState =  GPIO.input(GBUT)
        bButState =  GPIO.input(BBUT)
#        print('Button States:', rButState, gButState, bButState) 
        if rButStatePre != rButState:
            if rButState == 1:
                print('Red Button Pressed.')
                rLedState = not rLedState
                GPIO.output(RLED, rLedState)
            rButStatePre = rButState
        if gButStatePre != gButState:
            if gButState == 1:
                print('Green Button Pressed.')
                gLedState = not gLedState
                GPIO.output(GLED, gLedState)
            gButStatePre = gButState
        if bButStatePre != bButState:
            if bButState == 1:
                print('Blue Button Pressed.')
                bLedState = not bLedState
                GPIO.output(BLED, bLedState)
            bButStatePre = bButState
            
        sleep(DT)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('\n\rGPIO Good to Go.')

