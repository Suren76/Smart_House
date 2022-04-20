from Client import *
import time, socket, datetime, sys


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


# sensor = dht.DHT11(machine.Pin(4))
# do_connect()
client = Client()
print("socket 0")
client.connect("127.0.0.9", 1212)
address = client.data()
print(address,1)

server_status = client.data()
print(server_status,2)

if server_status != "data_mode":
    print("Error data_mode")
    sys.exit()

time.sleep(10)

while True:
    sensor.measure()
    client.send({"sensor": "dht", "address": address, "time": datetime.datetime.now(), "humidity": sensor.humidity(), "temperature": sensor.temperature()})
    time.sleep(60)

