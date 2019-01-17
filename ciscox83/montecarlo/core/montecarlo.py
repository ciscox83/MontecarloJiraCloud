from decimal import *
from random import randrange

from ciscox83.global_properties import MONTECARLO_ITERATIONS
from ciscox83.global_properties import ITERATION_DURATION


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

    def run(self, pending_items):
        average_iterations = []
        num_of_real_cycle_times = len(self.real_cycle_times)
        for x in range(0, MONTECARLO_ITERATIONS, 1):
            total_days = 0
            for y in range(0, num_of_real_cycle_times, 1):
                i = randrange(num_of_real_cycle_times)
                total_days = total_days + self.real_cycle_times[i]
            average_cycle_time = total_days / num_of_real_cycle_times
            average_iteration = round(pending_items * average_cycle_time / ITERATION_DURATION)
            average_iterations.append(average_iteration)
        return average_iterations