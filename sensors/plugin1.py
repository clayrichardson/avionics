import time

from random import randint

class Plugin1 (object):
  def __init__(self, shared):
    self.shared = shared

  def run(self):
    data = {
      'time': time.time(),
      'name': 'plugin1 is out of control',
      'value': randint(1, 10000)
    }
    return data
