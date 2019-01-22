class ProjectPivotEntry:
    def __init__(self, duration, count, percentage):
        self.duration = duration
        self.count = count
        self.percentage = percentage

    def get_duration(self):
        return self.duration

    def get_count(self):
        return self.count

    def get_percentage(self):
        return self.percentage