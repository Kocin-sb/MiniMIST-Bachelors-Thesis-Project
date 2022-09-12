# importing the dht and machine modules

import dht # measure dht11 sensor
from machine import Pin, ADC #GPIO pins in the module
from time import sleep
import esp32

sensordht = dht.DHT11(Pin(13))

def cel_to_fer(x):
    return x * (9/5) + 32.0

def readDht():
    sensordht.measure()
    temp = sensordht.temperature()
    tempf = cel_to_fer(temp)
    hum = sensordht.humidity()
    hall = esp32.hall_sensor()
    print("*** Remember that Hall sensor uses GPIO Pins 36 and 39, \nwhich are used by the camera on Freenove ESP32-Wrover Development board.\n\n")
    response = "Temperature in Celcius: "+str(temp)+"\nTemperature in Farenheit: "+str(tempf)+"\nHumidity: "+str(hum)+"\n Hall Sensor: " + str(hall)+"|"
    print(response)

while True:
    try:
        sleep(1)
        readDht()
    except OSError as e:
        print(e)
        print('Failed to read sensor.')
        
