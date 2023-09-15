import notify2

TITLE = "Alarm"
MESSAGE = "Alarm's time ended!"


def send_message():
    notify2.init("Test")
    notice = notify2.Notification(TITLE, MESSAGE)
    notice.show()
    return


if __name__ == "__main__":
    notify2.init("Test")
    print(notify2.get_server_caps())

    TITLE = "Alarm"
    MESSAGE = "Alarm has ended."

    notification = notify2.Notification(TITLE, MESSAGE)
    import os
    notification.show()
    os.system('spd-say "Test"')
