import time

class QueueSize(object):
  def __init__(self, shared):
    self.shared = shared

  def run(self):
    data = {
      'time': time.time(),
      'name': 'Queue Size',
      'value': self.shared.metrics.qsize()
    }
    return data
