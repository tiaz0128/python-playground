from datetime import datetime, UTC, timezone
from datetime import timedelta
import pytz
import json

utc_time = datetime.now(timezone.utc)
str_time = utc_time.strftime("%d/%m/%Y, %H:%M:%S")
a = json.dumps({"time": str_time})

print(utc_time)
print(str_time)
print(a)
