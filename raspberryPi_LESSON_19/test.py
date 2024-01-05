import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
PWMPIN = 18

GPIO.setup(PWMPIN, GPIO.OUT)
myPWM = GPIO.PWM(PWMPIN, 50)         # Period 20ms
myPWM.start(0)

# Duty Cycle vs Rotation:
# 0 degree      1% ~ 2%
# 180 degree    12% ~ 15%  

try:
    while True:
        pwmPercent = float(input('PWM %: '))
        myPWM.ChangeDutyCycle(pwmPercent)
        print('PWM % Your Enterred: ', pwmPercent)
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go.')