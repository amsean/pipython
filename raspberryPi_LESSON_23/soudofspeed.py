# Measuring (SoS) Speed of Soud with the HC-SR04 Ultrasonic Sensor

# 1ft = 12 inches, 1mile = 5280ft
# r = d / t
#   = 16 inches / pt seconds        
#   = (16 / ptt) [3600/(12*5280)] (miles/hour)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIGPIN = 23
ECHOPIN = 24
GPIO.setup(TRIGPIN, GPIO.OUT)
GPIO.setup(ECHOPIN, GPIO.IN)

try:
    while True:
        GPIO.output(TRIGPIN, 0)                     # send trig pulse signal
        time.sleep(2E-6)                            # 2us low
        GPIO.output(TRIGPIN, 1)         
        time.sleep(10E-6)                           # 10us high
        GPIO.output(TRIGPIN, 0)

        while GPIO.input(ECHOPIN) == 0:
            pass
        echoStartTime = time.time()
        while GPIO.input(ECHOPIN) == 1:
            pass
        echoStopTime = time.time()

        ptt = echoStopTime - echoStartTime                      # Ping Travel Time
        sos = 16 / ptt * 3600/(12*5280)                         # speed of soud
        print('The Speed of Soud: ', round(sos, 1), ' MPH')     # MPH

        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nGPIO Good to GO.')