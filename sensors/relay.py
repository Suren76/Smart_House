from Client import *
import time, machine, dht, network, socket, datetime, sys


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Raspberry', '3.141592')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


relay = machine.Pin(5, machine.Pin.OUT)
relay.value(0)
status = "off"

do_connect()
client = Client()
client.connect("192.168.18.120", 12125)
address = client.data()

server_status = client.data()

if server_status != "data_mode":
    print("Error data_mode")
    sys.exit()

time.sleep(10)

while True:

    command = client.recv(1024)
    command = command.decode("utf-8")

    if not command:
        time.sleep(1)
        continue

    if command == "on":
        relay.value(0)
        status = "on"
    if command == "off":
        relay.value(1)
        status = "off"

    client.send({"sensor": "relay", "address": address, "time": datetime.datetime.now(), "status": status})
    # time.sleep(60)

