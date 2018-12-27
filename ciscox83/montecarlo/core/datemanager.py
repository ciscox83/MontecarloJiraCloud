from datetime import datetime
from datetime import timedelta


class DateManager:
    def __init__(self):
        pass

    @staticmethod
    def a_week_ago(today):
        today = today + " 23:59:59"
        today = datetime.strptime(today, "%Y/%m/%d %H:%M:%S")
        a_week_ago = today - timedelta(days=7)
        a_week_ago = a_week_ago.strftime("%Y/%m/%d %H:%M:%S")[:-9]
        return a_week_ago + " 00:00"
