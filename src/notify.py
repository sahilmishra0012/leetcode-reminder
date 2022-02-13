from plyer import notification
import time
import datetime
import api

while(True):
    submission_count, remindinterval, notificationduration = api.get_current_submissions()
    if(submission_count==0):
        notification.notify(
            title = "LeetCode Statistics on {}".format(datetime.date.today()),
            message = "You have not made any submissions today!",
            # app_icon = "/home/samkiller007/leetcode/res/icons/bell-icon.ico",
            timeout  = notificationduration)
    # else:
    #     if(submission_count==1):
    #         notification.notify(
    #             title = "LeetCode Statistics on {}".format(datetime.date.today()),
    #             message = "Yeyy!! You have made 1 submission today!",
    #             app_icon = "/home/samkiller007/leetcode/res/icons/bell-icon.ico",
    #             timeout  = notificationduration)
    #     else:
    #         notification.notify(
    #             title = "LeetCode Statistics on {}".format(datetime.date.today()),
    #             message = "Yeyy!! You have made {} submissions today!".format(submission_count),
    #             app_icon = "/home/samkiller007/leetcode/res/icons/bell-icon.ico",
    #             timeout  = notificationduration)

    time.sleep(remindinterval)