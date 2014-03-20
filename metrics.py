
import gevent.monkey
gevent.monkey.patch_all()

from gevent.queue import Queue
from gevent.pool import Pool

import time
import requests
import json

from  random import randint

pool_size = 100
pool = Pool(pool_size)
metrics = Queue()

def send(data):
  with open("./logfile", "a") as outfile:
    outfile.write(json.dumps(data) + "\n")
  metrics.put_nowait(data)

def metric_metric1():
  while 1:
    data = {
      'time': time.time(),
      'name': 'metric1',
      'value': randint(1, 1000)
    }
    # print "queueing metric1"
    send(data)
    gevent.sleep()

def metric_metric2():
  while 1:
    data = {
      'time': time.time(),
      'name': 'metric2',
      'value': randint(1, 1000)
    }
    # print "queueing metric2"
    send(data)
    gevent.sleep()

def metric_queue_size():
  while 1:
    data = {
      'time': time.time(),
      'name': 'queue size',
      'value': metrics.qsize()
    }
    # print "queueing metric2"
    send(data)
    gevent.sleep()

def metric_collector():
  while 1:
    metric = metrics.get()

    while 1:
      try:
        r = requests.post("http://127.0.0.1:5000", data=metric)
        print "Status: %s Metric: %s" % (r.status_code, metric)
        gevent.sleep()
      except:
        print "Request failed, retrying."
        continue
      break

for number in xrange(pool_size):
  if not pool.full():
    print "Spawning pool worker #%s" % number 
    pool.spawn(metric_collector)

gevent.joinall([
  gevent.spawn(metric_metric1),
  gevent.spawn(metric_metric2),
  gevent.spawn(metric_queue_size),
])

