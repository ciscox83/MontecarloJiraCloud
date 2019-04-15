class DistributionEntry:
    def __init__(self, duration, cumulative_percentage):
        self.duration = duration
        self.cumulative_percentage = cumulative_percentage

    def get_duration(self):
        return self.duration

    def get_cumulative_percentage(self):
        return self.cumulative_percentage