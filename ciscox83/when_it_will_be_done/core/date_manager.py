from datetime import datetime
from datetime import timedelta

from ciscox83.when_it_will_be_done.core.constants import WORKING_DAYS_IN_ITERATION, DAYS_IN_WEEK


class DateManager:
    def __init__(self):
        pass

    @staticmethod
    def adjust_iteration_end_date(input_date):
        try:
            date = datetime.strptime(input_date, "%Y/%m/%d")
        except ValueError:
            try:
                date = datetime.strptime(input_date, "%Y/%m/%d %H:%M")
            except ValueError:
                raise ValueError("Incorrect data format: " + input_date)
        return date.strftime("%Y/%m/%d %H:%M")[:-6] + " 23:59"

    @staticmethod
    def get_iteration_start_date(end_date):
        iteration_end_date = datetime.strptime(DateManager.adjust_iteration_end_date(end_date), "%Y/%m/%d %H:%M")
        weeks = WORKING_DAYS_IN_ITERATION / 5
        days = WORKING_DAYS_IN_ITERATION + weeks * 2
        a_week_ago = iteration_end_date - timedelta(days=days)
        a_week_ago = a_week_ago.strftime("%Y/%m/%d %H:%M")[:-6]
        return a_week_ago + " 00:00"

    @staticmethod
    def get_end_date(duration, input_date):
        today = datetime.strptime(input_date, "%Y/%m/%d")
        days = round(duration * DAYS_IN_WEEK)
        end_date = today + timedelta(days=days)
        return end_date.strftime("%Y/%m/%d")

