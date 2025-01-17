# Using SPI to communicate with the MAX6675 thermocouple sensor
# Due to using more than one MAX6675 sensor, it is not possible to use I2C

import machine as m
import time

# Define the SPI pins
sck = m.Pin(18, m.Pin.OUT)
mosi = m.Pin(23, m.Pin.OUT)
miso = m.Pin(19, m.Pin.IN)
cs = m.Pin(5, m.Pin.OUT)

# Create the SPI object
spi = m.SPI(1, baudrate=100000, polarity=0, phase=0)

# Function to read the temperature from the MAX6675 sensor

def read_temp():
    cs.value(0)
    time.sleep_ms(1)
    data = spi.read(2)
    cs.value(1)
    temp = (data[0] << 8 | data[1]) >> 3
    return temp * 0.25

# Main loop

while True:
    temp = read_temp()
    print('Temperature: ', temp)
    time.sleep(1)

# End of main.py