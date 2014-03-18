
import requests

from celery import Celery

app = Celery('metrics')
app.config_from_object('celeryconfig')

@app.task(default_retry_delay=10, max_retries=None)
def send_metrics(data):
  r = requests.post("http://127.0.0.1:5000", data=data)
  return r.status_code

