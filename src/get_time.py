from datetime import date
import time

def get_time(currentdatepattern, epochpattern):
    current_date = date.today().strftime(currentdatepattern)
    epoch = int(time.mktime(time.strptime(str(current_date), epochpattern)))
    return epoch