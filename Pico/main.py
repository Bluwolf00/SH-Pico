# Using SPI to communicate with the MAX6675 thermocouple sensor
# Due to using more than one MAX6675 sensor, it is not possible to use I2C

import machine as m
import time
import datetime
from MAX6675 import MAX6675
import network
import urequests
from WLAN import networkDetails
import mypysql as pym

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = str(networkDetails.SSID)
password = str(networkDetails.PASSWORD)

# print(ssid, password)

wlan.connect(ssid, password)

so = m.Pin(15, m.Pin.IN)
sck = m.Pin(13, m.Pin.OUT)
cs = m.Pin(14, m.Pin.OUT)
led = m.Pin(25, m.Pin.OUT)

thermo = MAX6675(sck, cs, so)

max_wait = 20
while max_wait > 0 and not wlan.isconnected():
    print("Connecting to WiFi...")
    time.sleep(1)
    max_wait -= 1

connection = pym.connect(host="192.168.1.104",
                         user="root",
                         password="Password123",
                         database="pico")

with connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM pico")
        result = cursor.fetchall()
        print(result)

while True:
    print(thermo.read())
    data = thermo.read()
    led.toggle()
    print("Temperature: ", data)

    print("Sending data to server")
    # r = urequests.get("http://www.google.com")
    # print(r.content)

    url = "https://example-website.com/api/temperature"

    json_data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "temperature": data,
        "location": "Kitchen"
    }

    r = urequests.post(url, json=json_data)
    time.sleep(1.1)