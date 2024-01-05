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

dcR = 100
dcG = 100
dcB = 100

myPWMr = GPIO.PWM(RLED, 100)
myPWMg = GPIO.PWM(GLED, 100)
myPWMb = GPIO.PWM(BLED, 100)

myPWMr.start(int(dcR))
myPWMg.start(int(dcG))
myPWMb.start(int(dcB))

try:
    while True:
        rButState =  GPIO.input(RBUT)
        gButState =  GPIO.input(GBUT)
        bButState =  GPIO.input(BBUT)
        print('Button States:', rButState, gButState, bButState) 
        if rButStatePre != rButState:
            if rButState == 1:
                dcR = dcR / 1.58
                if dcR < 1:
                    dcR = 100
                myPWMr.ChangeDutyCycle(dcR)
            rButStatePre = rButState
        if gButStatePre != gButState:
            if gButState == 1:
                dcG = dcG / 1.58
                if dcG < 1:
                    dcG = 100
                myPWMg.ChangeDutyCycle(dcG)
            gButStatePre = gButState
        if bButStatePre != bButState:
            if bButState == 1:
                dcB = dcB / 1.58
                if dcB < 1:
                    dcB = 100
                myPWMb.ChangeDutyCycle(dcB)
            bButStatePre = bButState
        print(dcR, dcG, dcB)
        sleep(DT)

except KeyboardInterrupt:
    GPIO.cleanup()
    print()
    print('GPIO Good to Go.')
    print()

