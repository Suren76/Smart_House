from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import os
import sys
import requests
import face_unlock
import json

ip = "192.168.43.140"

print(3)
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite://database.db'
# db = SQLAlchemy(app)
#
# class Dht():
#     pass

# temperature = open("sensors_data/dht/temperature.json", "a").read()
# humidity = open("sensors_data/dht/humidity.json", "a").read()
# relay = open("sensors_data/relay/relay.json", "a").read()

print(4)
@app.route("/")
@app.route("/home")
def index():
    if os.path.exists("../sensors_data/dht/"):
        latest_temperature = json.loads(open(f"../sensors_data/dht/{os.listdir('../sensors_data/dht/')[0]}/temperature.json", "r+").read())
    else:
        latest_temperature = ["no data"]

    if os.path.exists("../sensors_data/dht/"):
        latest_humidity = json.loads(open(f"../sensors_data/dht/{os.listdir('../sensors_data/dht/')[0]}/humidity.json", "r+").read())
        # [open(f"../sensors_data/dht/{os.listdir('../sensors_data/dht/')[0]}/humidity.json", "r+").read()][-1][0]

    else:
        latest_humidity = ["no data"]

    if os.path.exists("../sensors_data/dht/"):
        latest_relay = json.loads(open(f"../sensors_data/relay/{os.listdir('../sensors_data/relay/')[0]}/relay.json", "r+").read())
        print(latest_relay, type(latest_relay))
        # [open(f"../sensors_data/relay/{os.listdir('../sensors_data/relay/')[0]}/relay.json", "r+").read()][-1][0]
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
        temperature_sensor_main = [open(f"sensors_data/dht/{os.listdir('sensors_data/dht/')[0]}/temperature.json", "r+").read()][-1]
        temperature_daily = [open(f"sensors_data/dht/{os.listdir('sensors_data/dht/')[0]}/temperature_hour.json", "r+").read()]
        temperature_weekly = [open(f"sensors_data/dht/{os.listdir('sensors_data/dht/')[0]}/temperature_day.json", "r+").read()]
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
        humidity_sensor_main = [open(f"sensors_data/dht/{os.listdir('sensors_data/dht/')[0]}/humidity.json", "r+").read()][-1]
        humidity_daily = [open(f"sensors_data/dht/{os.listdir('sensors_data/dht/')[0]}/humidity_hour.json", "r+").read()]
        humidity_weekly = [open(f"sensors_data/dht/{os.listdir('sensors_data/dht/')[0]}/humidity_day.json", "r+").read()]
    else:
        humidity_sensor_main = ["no data"][0]
        humidity_daily = ["no data"]
        humidity_weekly = ["no data"]

    return render_template("humidity.html", humidity=[humidity_sensor_main, humidity_daily, humidity_weekly])


print(8)
@app.route("/relay/")
def relay():
    if os.path.exists("sensors_data/relay/relay.json"):
        relay_sensor_main = [open(f"sensors_data/relay/{os.listdir('sensors_data/relay/')[0]}/relay.json", "r+").read()][-1]
        relay_daily = [open(f"sensors_data/relay/{os.listdir('sensors_data/relay/')[0]}/relay_hour.json", "r+").read()]
        relay_weekly = [open(f"sensors_data/relay/{os.listdir('sensors_data/relay/')[0]}/relay_day.json", "r+").read()]
    else:
        relay_sensor_main = ["no data"][0]
        relay_daily = ["no data"]
        relay_weekly = ["no data"]

    return render_template("relay.html", relay=[relay_sensor_main, relay_daily, relay_weekly])


print(9)
@app.route("/relay/<string:command>")
def relay_cmd(command):
    requests.get(ip+f"/?relay={command}")
    print(command)


print(10)
@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/settings/<string:command>/<string:file_location>/<string:name>")
def settings_set(command, file_location, name):
    if command == "face_model_registration":
        pass
        face_unlock.face_model(name, model_data_type="video", video_path=file_location)
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

app.run(debug=True, host="0.0.0.0", port=80)

