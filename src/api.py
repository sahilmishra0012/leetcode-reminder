import requests
import json
from load_config import load_config
from get_time import get_time

def get_current_submissions():
    config = load_config()
    current_date = str(get_time(config['currentdatepattern'], config['epochpattern']))

    data = {"query": config["query"], "variables":{"username":config["username"]}}
    headers = {"Content-Type": config["contenttype"], "referer" : config["referer"]}

    response = requests.post(config["url"], json=data, headers=headers)
    
    status = response.json()["data"]["matchedUser"]["submissionCalendar"]
    status = json.loads(status)

    if current_date in status.keys():
        return status[current_date], int(config["remindinterval"]), int(config["notificationduration"])
    else:
        return 0, int(config["remindinterval"]), int(config["notificationduration"])