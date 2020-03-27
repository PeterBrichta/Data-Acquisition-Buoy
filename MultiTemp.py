import time
import tsys01
from time import sleep

sensor = tsys01.TSYS01()
sensor2 = tsys01.TSYS01(4)

while True:
  
  if not sensor.init():
    print("Error intializing sensor 1")
    exit(1)

  while True:
    if not sensor.read():
      print("Error reading sensor 1")
      exit(1)
  
    print("Temperature: %.2f" % sensor.temperature(tsys01.UNITS_Farenheit))
    sleep(1)
    break
    
    if not sensor2.init():
      print("Error intializing sensor 2")
      exit(1)

  while True:
    if not sensor2.read():
      print("Error reading sensor 2")
      exit(1)
  
    print("Temperature: %.2f" % sensor2.temperature(tsys01.UNITS_Farenheit))
    sleep(1)
    break
    
    
