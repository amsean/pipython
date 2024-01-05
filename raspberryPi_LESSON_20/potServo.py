# Controlling Position of a Servo With a Potentiometer

import RPi.GPIO as GPIO
import ADC0834
from time import sleep

GPIO.setmode(GPIO.BCM)
PWMPIN = 4
GPIO.setup(PWMPIN, GPIO.OUT)
myPWM = GPIO.PWM(PWMPIN, 50)        # 20ms = 50Hz
myPWM.start(0)

ADC0834.setup()

# IN    OUT
# 0     2
# 255   12
# m = (y1-y2)/(x1-x2) = 10/255
# y-y1 = m(x-x1)
# y-2 = (10/255)(x-0)
# y = (10/255)x + 2
# pwmVal = (10/255)analogVal + 2

try:
    while True:
        analogVal = ADC0834.getResult(0)        # channel 0
#        analogVal = float(input('Enter analog Value: '))
        pwmPercent = 10/255 * analogVal + 2
        print('pwmPercent: ', pwmPercent)
        myPWM.ChangeDutyCycle(pwmPercent)
        sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go.')