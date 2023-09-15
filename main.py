from datetime import datetime
from AlarmClock import AlarmClock
from AlarmClock import send_message

import time
import os

alarm_format = "%H:%M:%S"
alarm = input("New Alarm (HH:MM:SS): ")
check_for_custom_message = input("Do you want to set a custom message? (Y/N): ")
custom_message = str()
if check_for_custom_message == "Y":
    custom_message = input("Input your desired message: ")
else:
    custom_message = "Your alarm has ended."
alarm = datetime.strptime(alarm, alarm_format)
alarm_clock = AlarmClock(hours=alarm.hour, minutes=alarm.minute, seconds=alarm.second, current=datetime.now())
alarm_finished = alarm_clock.end_time()

print(f"Alarm duration: {alarm_clock}")

while not alarm_clock.alarm_has_ended():
    time.sleep(5)

send_message()
os.system(f'spd-say "{custom_message}"')
print("Alarm Ended.")
