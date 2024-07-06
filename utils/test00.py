
from datetime import datetime
from dateutil.relativedelta import relativedelta

date_time_str = "04/23/2024"
date_time_format = "%m/%d/%Y"

date_time_obj = datetime.strptime(date_time_str, date_time_format)

print(date_time_obj)
# Output: 2024-04-23 00:00:00

six_months_ago = date_time_obj - relativedelta(months=6)

print("Current date:", date_time_obj)
print("Date 6 months ago:", six_months_ago)
print(type(six_months_ago))