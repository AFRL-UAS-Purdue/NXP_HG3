# Bosch BME688 Gas Sensor

# # Required Hardware
Raspberry Pi Pico
BME688 breakout board
Micro SD card breakout board

# # Pin Connections
BME688 VIN to Pico 3V3 (Pin 36)
BME688 GND to Pico GND (Pin 38)
BME688 SCK to Pico GP10 (Pin 14)
BME688 SDO to Pico GP11 (Pin 15)
BME688 SDI to Pico GP12 (Pin 16)
BME688 CS to Pico GP13 (Pin 17)
Micro SD breakout board GND to Pico GND (Pin 38)
Micro SD breakout board VCC to Pico 3V3 (Pin 36)
Micro SD breakout board MISO to Pico GP2 (Pin 4)
Micro SD breakout board MOSI to Pico GP3 (Pin 5)
Micro SD breakout board SCK to Pico GP6 (Pin 9)
Micro SD breakout board CS to Pico GP7 (Pin 10)

This directory contains all the code and materials worked on for the Bosch BME 688 gas sensor.

# getEnviData.py
This Micropython code reads temperature, humidity, pressure, and CO2 data from a BME688 sensor every second and saves it, along with a timestamp, to a file called "enviData.csv" on a micro SD card.

# # Required Libraries
utime module: provides functions for working with time
BME688 module: provides functions for reading data from BME688 sensor
os module: provides functions for working with the operating system
sdcard module: provides functions for working with a micro SD card

# # How the code works
The code imports necessary libraries and initializes the BME688 sensor and SD card.
The code creates a file called "enviData.csv" on the SD card.
The code enters a loop that runs indefinitely, reading data from the BME688 sensor every second.
For each set of data, the code retrieves the current time and formats it into a string.
The code writes the timestamp and data to the "enviData.csv" file on the SD card.
The loop continues to run indefinitely until the code is stopped.
This code demonstrates how to read data from a BME688 sensor and write it to a file on a micro SD card using a Raspberry Pi Pico. The code can be modified to read data from other sensors or to write data to other types of storage media.

# enviData.csv
Example output file after running the code for 20 seconds.
