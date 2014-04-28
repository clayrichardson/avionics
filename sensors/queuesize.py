import time

class QueueSize(object):
  def __init__(self, shared):
    self.shared = shared

  def collect(self):
    data = {
      'time': time.time(),
      'name': 'Queue Size',
      'value': self.shared.metrics.qsize()
    }
    time.sleep(100)
    return data
