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
# Open CSV file for writing
filename = "/sd/enviData.csv"
try:
    f = open(filename, "w")
    f.write("Time,Temperature(C),Humidity(%),Pressure(hPa),CO2(ppm)\n")
except:
    print("Error: Failed to create file")

# Get data every second and write to CSV file
try:
    for i in range(20):
        try:
            temp = bme.temperature
            humidity = bme.humidity
            pressure = bme.pressure / 100.0
            gas_resistance = bme.gas_resistance / 1000.0
            print("Temperature: {:.2f} C".format(temp))
            print("Humidity: {:.2f} %".format(humidity))
            print("Pressure: {:.2f} hPa".format(pressure))
            print("Gas Resistance: {:.2f} kOhms".format(gas_resistance))
            
            t = time.localtime()
            current_time = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])
            current_date = "{:02d}-{:02d}-{}".format(t[1], t[2], t[0])
            f.write("{},{:.2f},{:.2f},{:.2f},{:.2f}\n".format(current_date + " " + current_time, temp, humidity, pressure, gas_resistance))
            f.flush()
        except Exception as e:
            print("Error: Failed to read BME688 sensor data")
            print(str(e))
        
        time.sleep(1)

except Exception as e:
    print("Error: Failed to write data to CSV file")
    print(str(e))

# Close the file and unmount the SD card
try:
    f.close()
    uos.umount("/sd")
    print("Data saved to", filename)
except:
    print("Error: Failed to close file and unmount SD card")
