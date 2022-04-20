from flask import Flask, render_template, url_for
import random
import os
import sys

print(1)
# server = sys.argv[1]

print(2)

server = None

# def servers(server_obj):
#     global server
#     server = server_obj
#
# servers()

print(3)
app = Flask(__name__)

# temperature = open("sensors_data/dht/temperature.json", "a").read()
# humidity = open("sensors_data/dht/humidity.json", "a").read()
# relay = open("sensors_data/relay/relay.json", "a").read()

print(4)
@app.route("/")
@app.route("/home")
def index():
    if os.path.exists("sensors_data/dht/temperature.json"):
        latest_temperature = [open("sensors_data/dht/temperature.json", "r+").read()][-1]
    else:
        latest_temperature = ["no data"]

    if os.path.exists("sensors_data/dht/humidity.json"):
        latest_humidity = [open("sensors_data/dht/humidity.json", "r+").read()][-1]
    else:
        latest_humidity = ["no data"]

    if os.path.exists("sensors_data/dht/relay.json"):
        latest_relay = [open("sensors_data/relay/relay.json", "r+").read()][-1]
    else:
        latest_relay = ["no data"]

    return render_template("index.html", sensors_data=[latest_temperature, latest_humidity, latest_relay])


print(5)
@app.route("/scenario")
def scenario():
    return render_template("scenario.html")


print(6)
@app.route("/temperature")
def temperature():
    if os.path.exists("sensors_data/dht/temperature.json"):
        temperature_sensor_main = [open("sensors_data/dht/temperature.json", "r+").read()][-1]
        temperature_daily = [open("sensors_data/dht/temperature.json", "r+").read()]
        temperature_weekly = [open("sensors_data/dht/temperature.json", "r+").read()]
    else:
        temperature_sensor_main = ["no data"][0]
        temperature_daily = ["no data", "no data", "no data", "no data", "no data", "no data", "no data", "no data",
                             "no data", "no data", "no data", "no data"]
        temperature_weekly = ["no data", "no data", "no data", "no data", "no data", "no data"]

    return render_template("temperature.html",
                           temperature=[temperature_sensor_main, temperature_daily, temperature_weekly])


print(7)
@app.route("/humidity")
def humidity():
    if os.path.exists("sensors_data/dht/humidity.json"):
        humidity_sensor_main = [open("sensors_data/dht/humidity.json", "r+").read()][-1]
        humidity_daily = [open("sensors_data/dht/humidity.json", "r+").read()]
        humidity_weekly = [open("sensors_data/dht/humidity.json", "r+").read()]
    else:
        humidity_sensor_main = ["no data"][0]
        humidity_daily = ["no data"]
        humidity_weekly = ["no data"]

    return render_template("humidity.html", humidity=[humidity_sensor_main, humidity_daily, humidity_weekly])


print(8)
@app.route("/relay/")
def relay():
    if os.path.exists("sensors_data/relay/relay.json"):
        relay_sensor_main = [open("sensors_data/relay/relay.json", "r+").read()][-1]
        relay_daily = [open("sensors_data/relay/relay.json", "r+").read()]
        relay_weekly = [open("sensors_data/relay/relay.json", "r+").read()]
    else:
        relay_sensor_main = ["no data"][0]
        relay_daily = ["no data"]
        relay_weekly = ["no data"]

    return render_template("relay.html", relay=[relay_sensor_main, relay_daily, relay_weekly])


print(9)
@app.route("/relay/<string:command>")
def relay_cmd(command):
    if command == "on":
        print("on")
        return server.name
        # for i in server().address_list:
        #     i.send("on")
    if command == "off":
        print("off")
        return command
        # for i in server().address_list:
        #     i.send("off")
    if command == "random":
        command = str(str(random.randint(0, 9)) * 33 + " ") * 5
        return str(str(str(command + "\n") * 15) + "\n") * 555


print(10)
@app.route("/settings")
def settings():
    return render_template("settings.html")


print(11)
@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/name")
# def name():
#     return "name"
#
#
# @app.route("/name/<string:n>")
# def name(n):
#     return n

print(server, 1)
app.run(debug=True, host="0.0.0.0", port=9090)
print(server, 2)
