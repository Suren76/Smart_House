import time
import json
from Server import *
import os
from gpiozero import Button
import keyboard
import requests

ip1 = "192.168.43.140"
ip2 = "192.168.43.37"
ip3 = "192.168.43.6"


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

# time.sleep(60*3)

for_hour = 0
for_day = 0

while True:
    response1 = requests.get('http://' + ip1).json()
    response2 = requests.get('http://' + ip2).json()
    response3 = requests.get('http://' + ip3).json()

    responses = [response1, response2, response3[0], response3[1]]

    for response in responses:
        for_hour += 1
        for data in response:
            print(data)

        if not os.path.exists(f"sensors_data/{response['sensor']}"):
            os.mkdir(f"sensors_data/{response['sensor']}")
        # universal
        # file = open(f"sensors_data/{data['sensor']}/{data['sensor']}.json")

        # : dht, "humidity": sensor.humidity(), "temperature": sensor.temperature()
        if response["sensor"] == "dht":
            if not os.path.exists(f"sensors_data/{response['sensor']}/{response['name']}"):
                os.mkdir(f"sensors_data/{response['sensor']}/{response['name']}")

            # os.system(f"humidity={data['humidity']}")
            # os.system(f"temperature={data['temperature']}")
            data_temperature = {"time": response['time'], "temperature": response['temperature']}
            open(f"sensors_data/dht/{response['name']}/temperature.json", "w").write(str(json.dumps(data_temperature)))
            # open(f"sensors_data/dht/{response['name']}/temperature.json", "a").write(str(json.dumps(data_temperature))+',')

            data_humidity = {"time": response['time'], "humidity": response['humidity']}
            open(f"sensors_data/dht/{response['name']}/humidity.json", "w").write(str(json.dumps(data_humidity)))
            # open(f"sensors_data/dht/{response['name']}/humidity.json", "a").write(str(json.dumps(data_humidity))+',')
            # open(f"sensors_data/dht/humidity.json", "a").write(str(data_humidity))


            # template = "{% block temperature %}"+ data['temperature'] +"{% endblock %} \n\n{% block humidity %}"+ data['humidity'] +"{% endblock %}"
            # open("sensors_data/dht/dht.json", "w").write(str(template))

        # {"sensor": "relay", "time": datetime.datetime.now(), "status": status}
        if response["sensor"] == "relay":
            if not os.path.exists(f"sensors_data/{response['sensor']}/{response['name']}"):
                os.mkdir(f"sensors_data/{response['sensor']}/{response['name']}")

            data_relay = {"time": response['time'], "status": response['status']}
            open(f"sensors_data/relay/{response['name']}/relay.json", "w").write(str(json.dumps(data_relay)))
            # open(f"sensors_data/relay/{response['name']}/relay.json", "a+").write(str(json.dumps(data_relay))+',')
            # open(f"sensors_data/relay/relay.json", "a").write(str(data_relay))


            # template = "{% block relay %}"+ data['status'] +"{% endblock %}"
            # open("sensors_data/dht/dht.html", "w").write(str(template))




        if for_hour == 60:
            for data in response:
                if response["sensor"] == "dht":
                    data_temperature = {"time": response['time'], "temperature": response['temperature']}
                    open(f"sensors_data/dht/{response['name']}/temperature_hour.json", "a").write(str(data_temperature))

                    data_humidity = {"time": response['time'], "humidity": response['humidity']}
                    open(f"sensors_data/dht/{response['name']}/humidity_hour.json", "a").write(str(data_humidity))
                    # open(f"sensors_data/dht/humidity_hour.json", "a").write(str(data_humidity))

                if response["sensor"] == "relay":
                    data_relay = {"time": response['time'], "status": response['status']}
                    open(f"sensors_data/relay/{response['name']}/relay_hour.json", "a").write(str(data_relay))
                    # open(f"sensors_data/relay/relay_hour.json", "a").write(str(data_relay))


            for_hour = 0
            for_day += 1

        if for_day == 24:
            for data in response:
                if response["sensor"] == "dht":
                    data_temperature = {"time": response['time'], "temperature": response['temperature']}
                    open(f"sensors_data/dht/{response['name']}/temperature_day.json", "a").write(str(data_temperature))

                    data_humidity = {"time": response['time'], "humidity": response['humidity']}
                    open(f"sensors_data/dht/{response['name']}/humidity_day.json", "a").write(str(data_humidity))
                    # open(f"sensors_data/dht/humidity_hour.json", "a").write(str(data_humidity))

                if response["sensor"] == "relay":
                    data_relay = {"time": response['time'], "status": response['status']}
                    open(f"sensors_data/relay/{response['name']}/relay_day.json", "a").write(str(data_relay))
                    # open(f"sensors_data/relay/relay_hour.json", "a").write(str(data_relay))

            for_day = 0

    time.sleep(60)

