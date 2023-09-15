from datetime import datetime
from AlarmClock import AlarmClock
from AlarmClock import send_message

import time
import os

alarm_format = "%H:%M:%S"
alarm = input("New Alarm (HH:MM:SS): ")
alarm = datetime.strptime(alarm, alarm_format)
alarm_clock = AlarmClock(hours=alarm.hour, minutes=alarm.minute, seconds=alarm.second, current=datetime.now())
alarm_finished = alarm_clock.end_time()

print(f"Alarm duration: {alarm_clock}")

while not alarm_clock.alarm_has_ended():
    time.sleep(5)

send_message()
os.system('spd-say "Your Alarm has ended."')
print("Alarm Ended.")
