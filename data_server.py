from Server import *
import os
from gpiozero import Button
import keyboard


# button_connection_end = Button(17)
# button_data_server = Button(27)
print("socket server 0")
server = Server("127.0.0.9", 1212)
print("socket server 1")

print("mode_connection 0")
# server.mode_connection(button_connection_end.is_pressed)
server.mode_connection(keyboard.is_pressed("q"))
print("mode_connection 1")

# button_data_server.wait_for_press()
keyboard.wait("s")
# os.system(f"sudo python app.py {server}")
server.mode_data()

while True:
    data = server.data()

    if not os.path.exists(f"sensors_data/{data['sensor']}"):
        os.mkdir(f"sensors_data/{data['sensor']}")
    # universal
    # file = open(f"sensors_data/{data['sensor']}/{data['sensor']}.json")

    # : dht, "humidity": sensor.humidity(), "temperature": sensor.temperature()
    if data["sensor"] == "dht":
        # os.system(f"humidity={data['humidity']}")
        # os.system(f"temperature={data['temperature']}")
        data_temperature = {"time": data['time'], "temperature": data['temperature']}
        open("sensors_data/dht/temperature.json", "a").write(str(data_temperature))

        data_humidity = {"time": data['time'], "humidity": data['humidity']}
        open("sensors_data/dht/humidity.json", "a").write(str(data_humidity))

        # template = "{% block temperature %}"+ data['temperature'] +"{% endblock %} \n\n{% block humidity %}"+ data['humidity'] +"{% endblock %}"
        # open("sensors_data/dht/dht.json", "w").write(str(template))

    # {"sensor": "relay", "time": datetime.datetime.now(), "status": status}
    if data["sensor"] == "relay":

        data_relay = {"time": data['time'], "status": data['status']}
        open(f"sensors_data/relay/relay{data['address']}.json", "a").write(str(data_relay))

        # template = "{% block relay %}"+ data['status'] +"{% endblock %}"
        # open("sensors_data/dht/dht.html", "w").write(str(template))

