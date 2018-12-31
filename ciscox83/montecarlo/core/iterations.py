class Iteration:
    def __init__(self, completed, start_date, end_date):
        self.completed = completed
        self.start_date = start_date
        self.end_date = end_date

    def get_completed(self):
        return self.completed

    def set_completed(self, number):
        self.completed = number

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date