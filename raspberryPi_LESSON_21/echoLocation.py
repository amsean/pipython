# Using a HC-SR04 Ultrasonic Sensor For Echolocation
# Vcc, Trig, Echo, Gnd
# Trig:     2us(low) -> 10us(high)  
# Echo:     t 

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

        pingTravelTime = echoStopTime - echoStartTime
        print('pingTravelTime = ', int(pingTravelTime * 1E6), ' seconds')
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go.')
