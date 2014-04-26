import time

from random import randint
from lib import Adafruit_BMP085

class TempPress(object):
  def __init__(self, shared):
    self.shared = shared
    self.sensor = Adafruit_BMP085.BMP085()

  def collect(self):
    data = [
      {
        'time': time.time(),
        'name': 'pressure',
        'value': self.sensor.readPressure()
      },
      {
        'time': time.time(),
        'name': 'temperature',
        'value': self.sensor.readTemperature()
      },
      {
        'time': time.time(),
        'name': 'altitude',
        'value': self.sensor.readAltitude()
      }
    ]
    time.sleep(0.01)
    return data
