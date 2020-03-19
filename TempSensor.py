import time
import board
import busio
import adafruit_tca9548a
import tsys01

i2c = busio.I2C(board.SCL, board SDA)

tca = adafruit_tca9548.TCA9548A(I2C)

temp1 = tsys01.TSYS01(tca[0])
temp2 = tsys01.TSYS01(tca[1])

if not temp1.init():
  print("Error initializing temp. sensor 1")
  exit(1)
  
if not temp2.init():
  print("Error initializing temp. sensor 2")
  exit(1)
  
while True:
  if not temp1.read():
    print("Error reading sensor")
    exit(1)
    
while True:
  if not temp2.read():
    print("Error reading sensor")
    exit(1)
    
    print("Temperature: %.2f C\t%.2f F" % (temp1.temperature(tsys01.UNITS_Farenheit), temp2.temperature(tsys01.UNITS_Farenheit))
    sleep(0.2)

