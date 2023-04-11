import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds= [21,20,16,12,7,8,25,24]
comp=4
troyka=17
gpio.setup(dac, gpio.OUT)
gpio.setup(leds,gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def get_bin(a):
    return [int(element) for element in bin(a)[2:].zfill(8)]

def adc():
    dac_bin=[0,0,0,0,0,0,0,0]
    for i in range(0,8):
        dac_bin[i]=1
       #  print(dac_bin)
        gpio.output(dac,dac_bin)
        value=gpio.input(comp)
        time.sleep(0.01)
        if value==0:
            dac_bin[i]=0  
    return dac_bin

def get_volume(k):
    k=int(k/55*8)
    massive=[0]*8
    for i in range(k):
        massive[i]=1
    return massive

try:
    while True:
        binary=adc()
        i=binary[0]*128+binary[1]*64+binary[2]*32+binary[3]*16+binary[4]*8+binary[5]*4+binary[6]*2+binary[7]*1+1
        if i!=0:
            gpio.output(leds,get_volume(i))    
            print(3.3*i/256, "v", sep="")

finally:
    gpio.output(dac,0)
    gpio.cleanup()
