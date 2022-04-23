# This file is executed on every boot (including wake-boot from deepsleep)
import network
import esp
import uos
import machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import usocket as socket
import time
import json
import sys
import os
import dht

run_mode = "main"

# network.WLAN(network.STA_IF).disconnect()


wifi_networks = {"main":
                     ['Raspberry', '3.141592'],
                 "reserve":
                     ['BALCONY', '273824ha']
                 }


def do_connect(ssid, password):
    t = 10
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected() and t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            pass
        if not sta_if.isconnected():
            print("exit")
            return False
    print('network config:', sta_if.ifconfig())
    return sta_if.ifconfig()


# import webrepl
# webrepl.start()
print("main", 1)
main = do_connect(wifi_networks['main'][0], wifi_networks['main'][1])
print("main", 2)

if main == False:
    run_mode = "reserve"
    print("reserve", 1)
    reserve = do_connect(wifi_networks['reserve'][0], wifi_networks['reserve'][1])
    print("reserve", 2)

    if reserve == False:
        run_mode = "quit"
        sys.exit()
    else:
        ip = reserve[0]
else:
    ip = main[0]
    print(ip)

if "config.json" in os.listdir():
    with open("config.json", "r+") as file:
        config = json.loads(file.read())
        name = config['name']

if not "config.json" in os.listdir():
    with  open("config.json", "w+") as file:
        file.write(json.dumps({'name': str('nodemcu_' + ip)}))
    name = str('nodemcu' + ip)

led = machine.Pin(2, machine.Pin.OUT)
sensor = dht.DHT11(machine.Pin(5))
relay = machine.Pin(4, machine.Pin.OUT)

print(run_mode, name)