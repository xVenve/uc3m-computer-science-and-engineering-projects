
import paho.mqtt.client as mqtt
import time
from datetime import datetime

location = ""
id_device = ""

def on_connect(rc):
    if rc == 0:
        print("Connected success")
    else:
        print("Connected fail with code", {rc})


client = mqtt.Client()


def make_connection():
    client.username_pw_set(username="dso_server27", password="JoCa18")
    client.on_connect = on_connect
    client.will_set('/uc3m/classrooms/leganes/myclass/device_info', id_device + "," + location + "," + datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S") + ",Desconectado")
    client.connect("35.242.227.79", 1883, 60)  # IP MQTT


def send_temperature(temperature, time, device):
    client.publish('/uc3m/classrooms/leganes/myclass/temperature', payload=str(temperature)+","+str(time)+","+str(device), qos=0, retain=False)
    time.sleep(1)


def send_humidity(humidity, time, device):
    client.publish('/uc3m/classrooms/leganes/myclass/humidity', payload=str(humidity)+","+str(time)+","+str(device), qos=0, retain=False)
    time.sleep(1)


def send_id(identifier):
    global location, id_device
    data = identifier.split(",")
    id_device = data[0]
    location = data[1]
    client.publish('/uc3m/classrooms/leganes/myclass/device_info', payload=identifier, qos=0, retain=False)
    time.sleep(1)
