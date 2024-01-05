import RPi.GPIO as GPIO
import ADC0834
from time import sleep


RLED = 23
GLED = 24
BLED = 21
GPIO.setmode(GPIO.BCM)

GPIO.setup(RLED, GPIO.OUT)
GPIO.setup(GLED, GPIO.OUT)
GPIO.setup(BLED, GPIO.OUT)

myPWMr = GPIO.PWM(RLED, 1000)
myPWMg = GPIO.PWM(GLED, 1000)
myPWMb = GPIO.PWM(BLED, 1000)

myPWMr.start(0)
myPWMg.start(0)
myPWMb.start(0)

ADC0834.setup()

try:
    while True:
        analogR = ADC0834.getResult(0)
        analogG = ADC0834.getResult(1)
        analogB = ADC0834.getResult(2)
        print('RawRed = ', analogR, 'RawGreen = ', analogG, 'RawBlue = ', analogB)
        dcR = analogR / 2.55
        dcG = analogG / 2.55
        dcB = analogB / 2.55
        if dcR <= 3:
            dcR = 0
        if dcG <= 3:
            dcG = 0
        if dcB <= 3:
            dcB = 0
        myPWMr.ChangeDutyCycle(dcR)
        myPWMg.ChangeDutyCycle(dcG)
        myPWMb.ChangeDutyCycle(dcB)

        sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go.')