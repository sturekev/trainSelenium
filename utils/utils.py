
from datetime import datetime
from dateutil.relativedelta import relativedelta

class time_Measurement ():
    def __init__(self,last_measurement) -> None:
        self.last_measuremnt  = last_measurement
        
    def traverse_time_str_to_array (date_time_str: str):
        # 04/23/2024
        date_time_format = "%m/%d/%Y"

        date_time_obj = datetime.strptime(date_time_str, date_time_format)

        print(date_time_obj)
        # Output: 2024-04-23 00:00:00

        six_months_ago = date_time_obj - relativedelta(months=6)
        return type(six_months_ago)