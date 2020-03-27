import time
import board
import busio
import adafruit_tca9548a
import tsys01
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)

tca = adafruit_tca9548a.TCA9548A(i2c)

sensor = tsys01.TSYS01(tca[0])

while True:
  if not sensor.read():
    print("Error reading sensor")
    exit(1)
  
  print("Temperature: %.2f" % sensor.temperature(tsys01, UNITS_Farenheit))
  sleep(0.2)
