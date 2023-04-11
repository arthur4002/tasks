import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp=4
troyka=17
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def get_bin(a):
    return [int(element) for element in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        dac_bin=get_bin(i)
        gpio.output(dac,dac_bin)
        value=gpio.input(comp)
        time.sleep(0.001)
        if value==0:
            return i

try:
    while True:
        i=adc()
        if i!=0:
            print(3.3*i/256, "v", sep="")

finally:
    gpio.output(dac,0)
    gpio.cleanup()