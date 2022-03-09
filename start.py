import json
from pathlib import Path

import pypresence
import time

jsonfiledata = Path("data.json").read_text()
data = json.loads(jsonfiledata)

kWh = data["sum"] + data["today"]
sun = ''

if data["today"] < 100:
    sun = "☁️"
if data["today"] > 100:
    sun = "🌥️"
if data["today"] > 500:
    sun = "🌤️"
if data["today"] > 1200:
    sun = "☀️"

playNow = "🔋 {:3.0f} kWh & heute ".format(kWh / 1000)
if data["record"] < data["today"]:
    playNow += "🏆 "
playNow += " " + sun + "{:4.0f} Wh".format(data["today"])

print(kWh)
print(playNow)


def discord_rpc():
    id = Path("id.txt").read_text()
    RPC = pypresence.Presence(id)
    RPC.connect()
    RPC.update(state=playNow)


i = 0
while True:
    try:
        i = i + 1
        discord_rpc()
    except ConnectionError:
        print("Keine Verbindung!", i)

    time.sleep(20000)
