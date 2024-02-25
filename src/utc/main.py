from datetime import datetime

date_string = "2023-12-25 00:00:00+09:00"
date_format = "%Y-%m-%dT%H:%M:%S+09:00"

# datetime 객체로 변환
datetime_obj = datetime.fromisoformat(date_string)
print(datetime_obj.tzinfo)
