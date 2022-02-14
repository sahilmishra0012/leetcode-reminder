# LeetCode Reminder

!! Use codebase from dev branch only. Main branch is undergoing maintenance.

<div align="center">
  <img src="res/images/leetcode-reminder-logo.png" width="40%" 
     height="40%">
</div>

## Install

The current installation procedure has only been tested on `Manjaro Linux x86_64`. Raise an issue if it doesnt work for you.

1. Clone this repository to your system:

```
git clone https://github.com/sahilmishra0012/leetcode-reminder.git
```

2. Edit the configuration file. Edit your username and time configuration accordingly.

```
cd leetcode-reminder/res/configs
```
```
vi config
```

```
[CREDENTIALS]
UserName=<Your-Username>
Referer=https://leetcode.com/

[API]
URL=https://leetcode.com/graphql/
ContentType=application/json; charset=utf-8
Query=query getUserProfile($username: String!) { matchedUser(username: $username) { submissionCalendar } } 

[DATE]
EpochPattern=%%Y-%%m-%%d %%H:%%M:%%S
CurrentDatePattern=%%Y-%%m-%%d 05:30:00

[TIME]
RemindInterval=60
NotificationDuration=10
```

3. Run the following command from root directory to  bundle a Python application and all its dependencies into a single package. 

```
pyinstaller --onefile src/notify.py --hiddenimport=plyer.platforms.linux.notification
```

You can find the package in `dist` directory.

```
ls dist
```

It will be named as `notify`.

4. Create a shell script to run the application.

```
echo "/home/samkiller007/notify &" > notify.sh
```

5. Copy the shell script to `/etc/profile.d` so that it runs automatically on system startup.

```
sudo cp notify.sh /etc/profile.d/notify.sh
```
