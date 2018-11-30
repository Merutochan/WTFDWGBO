#!/usr/bin/python3

import sys
import time
import os

if len(sys.argv) != 3:
	print("Missing or exceeding arguments!")
	print("Please use " + sys.argv[0] + "www.WEBSITE.com TIME_IN_SEC")
	print()
	exit()

website = sys.argv[1]
t = int(sys.argv[2])

print("Welcome to WHEN THE FUCK DOES " + website + " GO BACK ONLINE?")


while 1:
	ping = os.system("ping -c 1 " + website +">> /dev/null")
	if (ping==0):
		print(website + " is now online!")
		notify = str("notify-send 'Website is back online' '" + website + " is back online!'")
		print(notify)
		os.system(notify)
		quit()
	else:
		time.sleep(t)


