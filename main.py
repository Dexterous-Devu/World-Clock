
__author__ : '@rockdevu'

import pytz
from datetime import datetime

city_list = ['Asia/Kolkata', 'America/New_York', 'Europe/London']

for i in city_list:
    time_zone = pytz.timezone(i)
    print(f"Time in {(i.split('/'))[1]}", datetime.now(tz = time_zone))
