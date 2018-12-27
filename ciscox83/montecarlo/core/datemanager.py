from datetime import datetime
from datetime import timedelta


class DateManager:
    def __init__(self):
        pass

    # we assume for simplicity that iterations are 1 every week
    @staticmethod
    def iteration_start_date(iteration_end_date):
        iteration_end_date = iteration_end_date + " 23:59:59"
        iteration_end_date = datetime.strptime(iteration_end_date, "%Y/%m/%d %H:%M:%S")
        a_week_ago = iteration_end_date - timedelta(days=7)
        a_week_ago = a_week_ago.strftime("%Y/%m/%d %H:%M:%S")[:-9]
        return a_week_ago + " 00:00"

    @staticmethod
    def iteration_end_date(date):
        try:
            datetime.strptime(date, '%Y/%m/%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be yyy/mm/dd")
        return date + " 23:59:59"
