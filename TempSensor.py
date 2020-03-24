import time
import board
import busio
import adafruit_tca9548a
import tsys01

i2c = busio.I2C(board.SCL, board.SDA)

tca = adafruit_tca9548a.TCA9548A(I2C)

temp1 = tsys01.TSYS01(tca[0])

if not temp1.init():
  print("Error initializing temp. sensor 1")
  exit(1)
  
while True:
  if not temp1.read():
    print("Error reading sensor")
    exit(1)
    
    print("TemperatureSens1: %.2f" % temp1.temperature(tsys01.UNITS_Farenheit))
    print("")
    sleep(0.2)

