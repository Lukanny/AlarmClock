from datetime import datetime, timedelta


class AlarmClock:

    def __init__(self, **kwargs) -> None:
        """
        Class constructor with AlarmClock properties.

        Common arguments:
        hours - minutes - seconds: define alarm duration
        current: current time when alarm was created
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

    @property
    def alarm_creation_time(self):
        return self._config.get("current")

    def end_time(self):
        end_time = self.alarm_creation_time + timedelta(hours=self.hours, minutes=self.minutes, seconds=self.seconds)
        return end_time.time()

    def alarm_has_ended(self):
        result = False
        if datetime.now().time() >= self.end_time():
            result = True
        return result

    def __str__(self):
        alarm = f"{self.hours}h{self.minutes}m{self.seconds}s"
        return alarm
