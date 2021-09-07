#! /usr/bin/python3
# Keep the dough at 37°C

import os,time

def led(x):
    if x==1:
        os.system('curl-silent 192.168.1.136/led/on')
    else:
        os.system('curl-silent 192.168.1.136/led/off')

def temp():
     return eval(os.popen('bash get_temp').read())

def rele(x): # heat gun connected to a wifi-plug
    if x==1:
        os.system('curl-silent 192.168.1.62/5/on')
    else:
        os.system('curl-silent 192.168.1.62/5/off')
        
while True:
    t=temp()
    print(t)
    if t>37:
        led(0)
        rele(0)
    else:
        led(1)
        rele(1)
    time.sleep(10)
