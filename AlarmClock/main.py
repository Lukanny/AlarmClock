from datetime import datetime, timedelta
from AlarmClock.utils import send_message
import time

alarm = input("New Alarm (HH:MM:SS): ")
format = "%H:%M:%S"

alarm = datetime.strptime(alarm, format)

alarm_finished = timedelta(hours=alarm.hour, minutes=alarm.minute, 
                           seconds=alarm.second) + datetime.now()

print(f"See you at {alarm_finished.time()}")

while datetime.now().time() < alarm_finished.time():
    time.sleep(60)

send_message()
