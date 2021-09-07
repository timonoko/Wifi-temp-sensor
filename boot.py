def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Jorpakko', 'Salasana')
        while not sta_if.isconnected():
            pass
    print('IF network config:', sta_if.ifconfig())

do_connect() 

def do_not_connect():
    import network
    ap_if = network.WLAN(network.AP_IF)
    print('AP network config:', ap_if.ifconfig())
    ap_if.active(False)
    print('AP network config:', ap_if.ifconfig())
    
import gc
gc.collect()

import esp
esp.osdebug(None)

import os
print(os.listdir())

def ls():
    print(os.listdir())

import webrepl
webrepl.start()

#do_not_connect()

import temp_probe

