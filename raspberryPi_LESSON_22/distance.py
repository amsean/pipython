# Measuring Distance with the HC-SR04 Ultrasonic Sensor
# d = r * t
# d = 767(miles/hour) * ptt
# d = 767 * ptt * (5280*12/3600) (inch)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIGPIN = 23
ECHOPIN = 24

GPIO.setup(TRIGPIN, GPIO.OUT)
GPIO.setup(ECHOPIN, GPIO.IN)

try:
    while True:
        GPIO.output(TRIGPIN, 0)
        time.sleep(2E-6)
        GPIO.output(TRIGPIN, 1)
        time.sleep(10E-6)
        GPIO.output(TRIGPIN, 0)

        while GPIO.input(ECHOPIN) == 0:
            pass
        echoStartTime = time.time()
        while GPIO.input(ECHOPIN) == 1:
            pass
        echoStopTime = time.time()

        ppt = echoStopTime - echoStartTime          # Ping Travel Time
        distance = 767 * ppt * (5280*12/3600)       # inches
        dtt = distance / 2                          # distance to the target
        print(round(dtt, 1), ' Inches')

        time.sleep(.2)


except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to GO.')