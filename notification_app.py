import time
import os
from notify_run import Notify

# Initialize Notify object
notify = Notify()

# Set the information to send
info_msg = "Don't forget to take a break!"

# Set the interval in seconds
interval = 15 * 60 # 15 minutes

# Loop infinitely
while True:
    notify.send(info_msg)
    os.system('cls')
    time.sleep(interval)