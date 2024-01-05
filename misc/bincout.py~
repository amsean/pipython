
import RPi.GPIO as GPIO
import time 

LED = 17
ON = False
OFF = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, ON)
time.sleep(1)
GPIO.output(LED, OFF)
time.sleep(1)

GPIO.output(LED, ON)
time.sleep(1)
GPIO.output(LED, OFF)
time.sleep(1)

GPIO.cleanup()
