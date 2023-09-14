import unittest

from AlarmClock import AlarmClock


class TestAlarm(unittest.TestCase):

    def setUp(self) -> None:
        self.alarm = AlarmClock(
            hours=1,
            minutes=30,
            seconds=0
        )

    def test_hours(self):
        self.assertEqual(self.alarm.hours, 1)

    def test_minutes(self):
        self.assertEqual(self.alarm.minutes, 30)
    
    def test_seconds(self):
        self.assertEqual(self.alarm.seconds, 0)

    def test_alarm_is_not_none(self):
        self.assertIsNotNone(self.alarm)
