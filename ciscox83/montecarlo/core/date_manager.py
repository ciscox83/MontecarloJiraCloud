from datetime import datetime
from datetime import timedelta


class DateManager:
    def __init__(self):
        pass

    @staticmethod
    def adjust_iteration_end_date(date):
        try:
            date = datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Incorrect data format, should be yyyy/mm/dd but it's: " + date)
        return date.strftime("%Y/%m/%d %H:%M")[:-6] + " 23:59"

    # we assume for simplicity that iterations are 1 every week
    @staticmethod
    def get_iteration_start_date(end_date):
        iteration_end_date = datetime.strptime(DateManager.adjust_iteration_end_date(end_date), "%Y/%m/%d %H:%M")
        a_week_ago = iteration_end_date - timedelta(days=7)
        a_week_ago = a_week_ago.strftime("%Y/%m/%d %H:%M")[:-6]
        return a_week_ago + " 00:00"

