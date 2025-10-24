#!/usr/bin/env python3

import json
import logging
import random
import time
import sys
from datetime import datetime

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "@timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "app": "some_app"
        }
        return json.dumps(log_entry)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.INFO)

while True:
    number = random.randrange(0, 4)
    if number == 0:
        logging.info("Hello there!!")
    elif number == 1:
        logging.warning("Hmmm....something strange")
    elif number == 2:
        logging.error("OH NO!!!!!!")
    elif number == 3:
        try:
            raise Exception("this is exception")
        except Exception as e:
            logging.error(str(e))
    time.sleep(1)