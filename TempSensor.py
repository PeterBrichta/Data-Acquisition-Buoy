import time
from time import sleep
import board
import busio
import adafruit_tca9548a
import tsys01
import smbus2

rpi_bus_number = 1
multiplexer_address = 0x70
I2C_ch_0 = 0B00000001
I2C_ch_1 = 0B00000010
x = 1

bus = smbus2.SMBus(rpi_bus_number)

i2c = busio.I2C(board.SCL, board.SDA)

bus.write_byte(multiplexer_address, I2C_ch_0)

sensor = tsys01.TSYS01()

while x == 1:
    if not sensor.init():
      print("Error initializing sensor")
      exit(1)
      
    bus.write_byte(multiplexer_address, I2C_ch_0)
    sleep(60)

    while True:
      if not sensor.read():
        print("Error reading sensor")
        exit(1)

       print("TemperatureSens1: %.2f" % temp1.temperature(tsys01.UNITS_Farenheit))
       print("")
       sleep(60)
       break
     
     bus.write_byte(multiplexer_address, I2C_ch_1)
     sleep(60)
    
     while True:
      if not sensor.read():
        print("Error reading sensor")
        exit(1)
        
      print("TemperatureSens1: %.2f" % temp1.temperature(tsys01.UNITS_Farenheit))
      print("")
      sleep(60)
      break
      
     

