from plyer import notification
import time
import datetime
import api
from load_config import load_config
from network import check_connection

while(True):
    is_connected = check_connection()
    config = load_config()
    remindinterval = int(config["remindinterval"])
    notificationduration = int(config["notificationduration"])
    if(is_connected==True):
        submission_count = api.get_current_submissions()
        if(submission_count==0):
            notification.notify(
                title = "LeetCode Statistics on {}".format(datetime.date.today()),
                message = "You have not made any submissions today!",
                # app_icon = "/home/samkiller007/leetcode/res/icons/bell-icon.ico",
                timeout  = notificationduration)
        else:
            if(submission_count==1):
                notification.notify(
                    title = "LeetCode Statistics on {}".format(datetime.date.today()),
                    message = "Yeyy!! You have made 1 submission today!",
                    timeout  = notificationduration)
                break
            else:
                notification.notify(
                    title = "LeetCode Statistics on {}".format(datetime.date.today()),
                    message = "Yeyy!! You have made {} submissions today!".format(submission_count),
                    timeout  = notificationduration)
                break
        time.sleep(remindinterval)
    else:
        notification.notify(
                title = "LeetCode Statistics - Network Error",
                message = "Connect to internet!",
                timeout  = notificationduration)
        time.sleep(remindinterval)