# This file is executed on every boot (including wake-boot from deepsleep)
import network
import esp
import uos as os
import machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import usocket as socket
import time
import json


run_mode = "main"

esp.osdebug(None)

wifi_networks = {"main":
                     ['Raspberry', '3.141592'],
                 "reserve":
                     ['TeAm', '28500801']
                 }


def do_connect(ssid: str, password: str, delay: int = 5):
    t = 60*delay
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    while not sta_if.isconnected() and t > 0:
        sta_if.connect(ssid, password)
        print(t)
        t -= 1
        print(sta_if.isconnected())

        if sta_if.isconnected():
            print('connect')
            return sta_if.ifconfig()
        elif t == 0:
            print("time out")
            return False
        time.sleep(1)

        # print(sta_if.isconnected())

    print('network config:', sta_if.ifconfig())


# import webrepl
# webrepl.start()

main = do_connect(wifi_networks['main'][0], wifi_networks['main'][1])
ip = main[0]
if not main:
    run_mode = "reserve"
    reserve = do_connect(wifi_networks['reserve'][0], wifi_networks['reserve'][1])
    ip = reserve[0]
    if not reserve:
        run_mode = "quit"
        quit()

if not os.path.exists("config.json"):
    with  open("config.json", "w+") as file:
        file.write(json.dumps({'name': str('nodemcu'+ip)}))
    name = str('nodemcu'+ip)

if os.path.exists("config.json"):
    with open("config.json", "r+") as file:
        config = file.read()
        name = config['name']

led = machine.Pin(2, machine.Pin.OUT)
relay = machine.Pin(4, machine.Pin.OUT)





