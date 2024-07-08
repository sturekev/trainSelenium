
from datetime import datetime
from dateutil.relativedelta import relativedelta

class time_Measurement ():
    def __init__(self,last_measurement) -> None:
        self.last_measuremnt  = last_measurement
        
    def traverse_time_str_to_array (date_time_str:str):
        # 04/23/2024
        date_time_format = "%m/%d/%Y"

        date_time_obj = datetime.strptime(date_time_str, date_time_format)

        print(date_time_obj)
        # Output: 2024-04-23 00:00:00

        six_months_ago = date_time_obj - relativedelta(months=6)
        return six_months_ago
    
    def get_back_to_input_format (input):
        # Format the date as "MM/DD/YYYY"
        date_string = input.strftime("%m/%d/%Y")
        return date_string
    
class basic_analysis ():
    def __init__(self, data) -> None:
        self.db = data
        self.Systolic = None
        self.Diastolic = None
        self.HR_measurements = None 
    
    def get_min(self,target_col):
        res = []
        for dt_by_col in self.db: 
            res.append(dt_by_col[target_col])
        return min(res)
    
    def get_max(self,target_col):
        res = []
        for dt_by_col in self.db: 
            res.append(dt_by_col[target_col])
        return max(res)
    
    def get_average(self,target_col):
        sum = 0
        for dt_by_col in self.db: 
            sum += dt_by_col[target_col]
        
        return sum/len(self.db)
       
    def get_analysis_SYS (self):
        target_col = 3
        return {
            "Min": self.get_min(target_col),
            "Max": self.get_max(target_col),
            "Average": self.get_average(target_col)
        }
   
    def get_analysis_DIA (self):
        target_col = 4
        return {
            "Min": self.get_min(target_col),
            "Max": self.get_max(target_col),
            "Average": self.get_average(target_col)
        }
   
    def get_analysis_HR (self):
        target_col = 5
        return {
            "Min": self.get_min(target_col),
            "Max": self.get_max(target_col),
            "Average": self.get_average(target_col)
        }