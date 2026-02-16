from machine import Pin
import time

in1 = Pin(12, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(33, Pin.OUT)

list = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]

while True:
    for i in list:
        in1.value(i[0])
        in2.value(i[1])
        in3.value(i[2])
        in4.value(i[3])
        time.sleep(0.005)
