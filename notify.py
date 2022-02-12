from plyer import notification
import time
import datetime
import api

while(True):
    submission_count = api.get_current_submissions()
    if(submission_count==0):
        notification.notify(
            title = "LeetCode Statistics on {}".format(datetime.date.today()),
            message = "You have not made any submissions today! Go and Code!",
            app_icon = "Paomedia-Small-N-Flat-Bell.ico",
            timeout  = 10)
    else:
        if(submission_count==1):
            notification.notify(
                title = "LeetCode Statistics on {}".format(datetime.date.today()),
                message = "Yeyy!! You have made 1 submission today!",
                app_icon = "Paomedia-Small-N-Flat-Bell.ico",
                timeout  = 10)
        else:
            notification.notify(
                title = "LeetCode Statistics on {}".format(datetime.date.today()),
                message = "Yeyy!! You have made {} submissions today!".format(submission_count),
                app_icon = "Paomedia-Small-N-Flat-Bell.ico",                
                timeout  = 10)

    time.sleep(60)