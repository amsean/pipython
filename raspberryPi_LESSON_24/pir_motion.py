# Raspberry Pi LESSON 24: 
# Using a PIR Motion Sensor with the Raspberry Pi

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
PIRPIN = 12                     # pin on board

GPIO.setup(PIRPIN, GPIO.IN)
# wait for 10 seconds
sleep(10)                                   

try:
    while True:
        motion = GPIO.input(PIRPIN)
        print(motion)
        sleep(.1)  

except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nGPIO Good to Go')

