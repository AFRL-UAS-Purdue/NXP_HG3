import os
import time
import board
import busio
import adafruit_bme688
import adafruit_sdcard
import storage

# Define the pins
SD_CS = board.GP6
SD_SCK = board.GP10
SD_MOSI = board.GP11
SD_MISO = board.GP12

BME_CS = board.GP7
BME_SCK = board.GP9
BME_SDO = board.GP8
BME_SDI = board.GP4

# Set up the SD card
spi = busio.SPI(SD_SCK, SD_MOSI, SD_MISO)
cs = digitalio.DigitalInOut(SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# Set up the BME688 sensor
bme_spi = busio.SPI(BME_SCK, BME_SDI, BME_SDO)
bme_cs = digitalio.DigitalInOut(BME_CS)
bme_sensor = adafruit_bme688.Adafruit_BME688_SPI(bme_spi, bme_cs)

# Open the file
filename = "/sd/enviData.csv"
with open(filename, "w") as f:
    f.write("time,temp_c,humidity,pressure,co2\n")

# Read and write data every second
while True:
    # Get the current time
    current_time = time.monotonic()

    # Read the sensor data
    temp_c = bme_sensor.temperature
    humidity = bme_sensor.humidity
    pressure = bme_sensor.pressure
    co2 = bme_sensor.gas

    # Write the data to the file
    with open(filename, "a") as f:
        f.write("{},{},{},{},{}\n".format(current_time, temp_c, humidity, pressure, co2))

    # Wait for 1 second
    time.sleep(1)
