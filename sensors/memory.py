import time

from random import randint

class Memory (object):
  def __init__(self, shared):
    self.shared = shared

  def run(self):
    data = {
      'time': time.time(),
      'name': 'memory used',
      'value': randint(1, 1000)
    }
    return data
