from machine import Pin
import time

in1 = Pin(12, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(33, Pin.OUT)

list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
r_list = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

while True:
    for x in range(500):
        for a in list:
            in1.value(a[0])
            in2.value(a[1])
            in3.value(a[2])
            in4.value(a[3])
            time.sleep(0.003)
        
    for y in range(500):
        for k in r_list:
            in1.value(k[0])
            in2.value(k[1])
            in3.value(k[2])
            in4.value(k[3])
            time.sleep(0.003)
