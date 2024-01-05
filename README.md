# Python & Raspberry Pi GPIO

## Installing pip/setuptools/wheel

> - https://toptechboy.com/



```shell
sudo apt update && sudo apt install python3-venv python3-pip

# Ensure you can run pip from the command line
python3 -m pip --version

# 
sudo apt install python3-numpy
```



## Vim Setup

```shell
:nmap <F6> :w<CR>:!clear<CR>:!python %<CR>
# disable mouse in Vim
:set mouse=
```





```python
# 
round(num, 2)

# 
x = input('Input Your First Number: ')
y = input('Input Your Second Number: ')
x = int(x)
y = int(y)
# 
x = int(input('Input Your First Number: '))
x = float(input('Input Your First Number: '))

# String concatenating
'string1' + 'string2'

if x > 0:
    print('Positive!')
#    
x = 1
while x <= 10:
    print(x)
    x = x + 1
print('Thats all folks!') 

#
for i in range(0, 10, 1):
    print(i)
```



## Raspberry Pi GPIO

```python
python3							# Enter Python interpreter

## 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)		# Pinouts of on board
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)
GPIO.output(11, True)
GPIO.cleanup()

## 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)			# Pinouts of BCM
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)
GPIO.output(17, True)
ON = False
OFF = True
GPIO.output(17, ON)
GPIO.output(17, OFF)
GPIO.cleanup()

## 
import time
time.sleep(5)					# sleep for 5 seconds.
```



##  GPIO PWM

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
# Test GPIO Output
GPIO.output(26, 0)
GPIO.output(26, 1)

# Setup PWM with Parameters
myPWM = GPIO.PWM(26, 100)	# pin and frequency
myPWM.start(50)				# duty cycle
# Change PWM DC and Frequency
myPWM.ChangeDutyCycle(25)
myPWM.ChangeDutyCycle(75)
myPWM.ChangeFrequency(10)
myPWM.ChangeFrequency(60)

myPWM.stop()


```



## Dimmable LED with Two Push Buttons

```python
# myDim.py
import RPi.GPIO as GPIO
from time import sleep

DT = 0.1
BUT1 = 20
BUT2 = 21
but1State = 1
but1StatePre = 1
but2State = 1
but2StatePre = 1
LED = 26
dc = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
myPWM = GPIO.PWM(LED, 100)
myPWM.start(dc)

try:
    while True:
        but1State = GPIO.input(BUT1)
        but2State = GPIO.input(BUT2)
        if but1StatePre != but1State:
            if but1State == 1:
                dc = dc - 10
                print('Dim Event')
            but1StatePre = but1State
        if but2StatePre != but2State:
            if but2State == 1:
                dc = dc + 10
                print('Bright Event')
            but2StatePre = but2State
        if dc > 99:
            dc = 99
        if dc < 0:
            dc = 0
        myPWM.ChangeDutyCycle(dc)
        sleep(DT)

except KeyboardInterrupt:
        myPWM.stop()
        GPIO.cleanup()
        print('\r\nGPIO Good to GO')
```



## RGB LED

```python
# Bash
import RPi.GPIO as GPIO
RLED = 26
GLED = 19
BLED = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(GLED, GPIO.OUT)
GPIO.setup(RLED, GPIO.OUT)
GPIO.setup(BLED, GPIO.OUT)
GPIO.output(RLED, 1)		# OFF
GPIO.output(GLED, 1)
GPIO.output(BLED, 1)
GPIO.output(RLED, 0)		# ON
```



## Pushbutton Control of RGB LED

```python
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
```



## Set Color of RGB LED with Push Buttons

## Vpython: Visual Python

...

Lesson 14 on [Youtube](https://www.youtube.com/watch?v=_q5t46kIC30&list=PLGs0VKk2DiYxdMjCJmcP6jt4Yw6OHK85O&index=17)



## Analog Input: ADC0834

> [ADC0834 library](https://toptechboy.com/sunfounder-adc0834-analog-to-digital-chip-library-for-the-raspberry-pi/) for Raspberry Pi

```shell
mv ADC0834.py /usr/lib/python3.11/ADC0834.py
```



## Mixing Any Color on an RGB LED

## LESSON 18

Using a Joystick With the Raspberry Pi

## LESSON 19

Simple Control of [Servo](https://youtu.be/i7hMx6YLR0Q?si=EcIqNzME06Nh0k07) From Raspberry Pi



___



Youtube Tutorial[^1]



[1]: 