from decimal import *

class Montecarlo:
    def __init__(self, iterations):
        self.iterations = iterations
        pass

    def get_real_cycle_times(self):
        cycle_times = []
        for iteration in self.iterations:
            cycle_time = 5.0 / iteration.get_completed()
            cycle_times.append(Decimal(cycle_time).__round__(2))
        return cycle_times
