#!/usr/bin/python3

import sys
import time
import os
import smtplib
from email.mime.text import MIMEText

if len(sys.argv) != 3:
	print("Missing or exceeding arguments!")
	print("Please use " + sys.argv[0] + "www.WEBSITE.com TIME_IN_SEC")
	print()

website = sys.argv[1]
t = int(sys.argv[2])

print("Welcome to WHEN THE FUCK DOES " + website + " GO BACK ONLINE?")

HOST = 'tuohostsmtp'
USER = 'tuamail'
PSW = 'password'
TARGET = 'tuamail'

minute = time.localtime(4)

while 1:
	ping = os.system("ping -c 1 " + website)
	if (ping==0):
		print(website + " is now online!")
		msg = MIMEText('online')
		msg['Subject'] = website + "is now online"
		msg['From'] = USER
		msg['To'] = TARGET
		server =  smtplib.SMTP_SSL(HOST)
		server.login(USER, PSW)
		server.sendmail(USER, TARGET, msg.as_string())
		server.quit()
		quit()
	else:
		time.sleep(t)


