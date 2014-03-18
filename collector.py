
import time
import json
import requests

from random import randint

from metrics import send_metrics

while 1:
  data = {
    'key1': randint(1, 1000),
    'key2': randint(1, 1000),
  }

  # print "Sending metrics: %s" % data
  send_metrics.delay(data)
  #time.sleep(0.001)

