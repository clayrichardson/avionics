# Prerequisites

1. Install Redis: `brew install redis`
2. Install requirements via Pip: `pip install -r requirements.txt`

# Running the Avionics Services

Start redis
---
redis-server ./redis.conf

Start flask server
---
python ./server.py

Start celery worker
---
celery -A metrics worker --loglevel=debug

Start celery flower
---
celery flower


Installing redis on angstrom
---
https://github.com/adafruit/Adafruit-WebIDE/blob/master/scripts/install-angstrom.sh

