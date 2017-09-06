import paho.mqtt.client as paho
import pyautogui
import random

tran_data = ["enter", "up", "down", "left", "right", "f", "esc"]

channelid = "channel" + str(random.randint(0, 10000))

def on_connect(client, userdata, flags, rc):
    print("Connect complate!")
    client.subscribe(channelid)

def on_message(client, userdata, msg):
    dd = str(msg.payload, "utf-8")
    print(dd + " in " + channelid)
    pyautogui.press(dd)

client = paho.Client()
client.connect(<hostname>, 1883)
client.on_connect = on_connect
client.on_message = on_message

if __name__ == "__main__":
    print("channel id is : " + channelid)
    client.loop_forever()