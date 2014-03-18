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

