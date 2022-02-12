from datetime import date
import time

def get_time(config):
    current_date = date.today().strftime(config["currentdatepattern"])
    epoch = int(time.mktime(time.strptime(str(current_date), config["epochpattern"])))
    return epoch