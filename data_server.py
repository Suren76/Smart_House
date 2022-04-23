import time

from Server import *
import os
from gpiozero import Button
import keyboard
import requests

ip = "192.168.1.101"


# button_connection_end = Button(17)
# button_data_server = Button(27)
# print("socket server 0")
# server = Server("127.0.0.9", 1212)
# print("socket server 1")
#
# print("mode_connection 0")
# # server.mode_connection(button_connection_end.is_pressed)
# server.mode_connection(keyboard.is_pressed("q"))
# print("mode_connection 1")
#
# # button_data_server.wait_for_press()
# keyboard.wait("s")
# # os.system(f"sudo python app.py {server}")
# server.mode_data()

# ips_list = os.system("sudo arp")

time.sleep(60*3)

for_hour = 0
for_day = 0

while True:
    response = requests.get(ip)

    for data in response:

        if not os.path.exists(f"sensors_data/{data['sensor']}"):
            os.mkdir(f"sensors_data/{data['sensor']}")
        # universal
        # file = open(f"sensors_data/{data['sensor']}/{data['sensor']}.json")

        # : dht, "humidity": sensor.humidity(), "temperature": sensor.temperature()
        if data["sensor"] == "dht":
            # os.system(f"humidity={data['humidity']}")
            # os.system(f"temperature={data['temperature']}")
            data_temperature = {"time": data['time'], "temperature": data['temperature']}
            open(f"sensors_data/dht/{data['name']}/temperature.json", "a").write(str(data_temperature))

            data_humidity = {"time": data['time'], "humidity": data['humidity']}
            open(f"sensors_data/dht/{data['name']}/humidity.json", "a").write(str(data_humidity))
            # open(f"sensors_data/dht/humidity.json", "a").write(str(data_humidity))


            # template = "{% block temperature %}"+ data['temperature'] +"{% endblock %} \n\n{% block humidity %}"+ data['humidity'] +"{% endblock %}"
            # open("sensors_data/dht/dht.json", "w").write(str(template))

        # {"sensor": "relay", "time": datetime.datetime.now(), "status": status}
        if data["sensor"] == "relay":

            data_relay = {"time": data['time'], "status": data['status']}
            open(f"sensors_data/relay/{data['name']}/relay.json", "a").write(str(data_relay))
            # open(f"sensors_data/relay/relay.json", "a").write(str(data_relay))


            # template = "{% block relay %}"+ data['status'] +"{% endblock %}"
            # open("sensors_data/dht/dht.html", "w").write(str(template))


    for_hour += 1

    if for_hour == 60:
        for data in response:
            if data["sensor"] == "dht":
                data_temperature = {"time": data['time'], "temperature": data['temperature']}
                open(f"sensors_data/dht/{data['name']}/temperature_hour.json", "a").write(str(data_temperature))

                data_humidity = {"time": data['time'], "humidity": data['humidity']}
                open(f"sensors_data/dht/{data['name']}/humidity_hour.json", "a").write(str(data_humidity))
                # open(f"sensors_data/dht/humidity_hour.json", "a").write(str(data_humidity))

                data_relay = {"time": data['time'], "status": data['status']}
                open(f"sensors_data/relay/{data['name']}/relay_hour.json", "a").write(str(data_relay))
                # open(f"sensors_data/relay/relay_hour.json", "a").write(str(data_relay))


        for_hour = 0
        for_day += 1

    if for_day == 24:
        for data in response:
            if data["sensor"] == "dht":
                data_temperature = {"time": data['time'], "temperature": data['temperature']}
                open(f"sensors_data/dht/{data['name']}/temperature_day.json", "a").write(str(data_temperature))

                data_humidity = {"time": data['time'], "humidity": data['humidity']}
                open(f"sensors_data/dht/{data['name']}/humidity_day.json", "a").write(str(data_humidity))
                # open(f"sensors_data/dht/humidity_hour.json", "a").write(str(data_humidity))

                data_relay = {"time": data['time'], "status": data['status']}
                open(f"sensors_data/relay/{data['name']}/relay_day.json", "a").write(str(data_relay))
                # open(f"sensors_data/relay/relay_hour.json", "a").write(str(data_relay))

        for_day = 0

    time.sleep(60)

