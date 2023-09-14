from datetime import datetime, timedelta
from AlarmClock.utils import send_message
import time

alarm = input("New Alarm (HH:MM:SS): ")
alarm_format = "%H:%M:%S"

alarm = datetime.strptime(alarm, alarm_format)

alarm_finished = timedelta(hours=alarm.hour, minutes=alarm.minute, 
                           seconds=alarm.second) + datetime.now()

print(f"See you at {alarm_finished.time()}")

while datetime.now().time() < alarm_finished.time():
    time.sleep(60)

send_message()


class AlarmClock:

    def __init__(self, **kwargs) -> None:
        """
        Class constructor with AlarmClock properties.

        Common arguments:
        'hours' - how many hours the alarm has
        'minutes' - how many minutes the alarm has
        'seconds' - how many seconds the alarm has
        """
        self._config = kwargs
        if not self._config or len(self._config) == 0:
            raise RuntimeError("A non null value is expected.")
        
    @property
    def config(self):
        return self._config
    
    @property
    def hours(self):
        return self._config.get("hours")
    
    @property
    def minutes(self):
        return self._config.get("minutes")
    
    @property
    def seconds(self):
        return self._config.get("seconds")
    