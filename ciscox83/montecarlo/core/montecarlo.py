from decimal import *
from random import randrange

from ciscox83.global_properties import montecarlo_iterations


class Montecarlo:
    def __init__(self, iterations):
        self.iterations = iterations
        self.real_cycle_times = self.__compute_real_cycle_times()
        pass


    def get_real_cycle_times(self):
        return self.real_cycle_times

    def __compute_real_cycle_times(self):
        cycle_times = []
        for iteration in self.iterations:
            cycle_time = 5.0 / iteration.get_completed()
            cycle_times.append(Decimal(cycle_time).__round__(2))
        return cycle_times

    def run(self):
        cycle_time_averages = []
        num_of_real_cycle_times = len(self.real_cycle_times)
        for x in range(0, montecarlo_iterations, 1):
            total_days = 0
            for y in range(0, num_of_real_cycle_times, 1):
                i = randrange(num_of_real_cycle_times)
                total_days = total_days + self.real_cycle_times[i]
            average_cycle_time = total_days / num_of_real_cycle_times
            cycle_time_averages.append(average_cycle_time)
        return cycle_time_averages