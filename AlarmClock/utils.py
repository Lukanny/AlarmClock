import notify2

TITLE = "Alarm"
MESSAGE = "Alarm's time ended!"

def send_message():
    notify2.init("Test")
    notice = notify2.Notification(TITLE, MESSAGE)
    notice.show()
    return