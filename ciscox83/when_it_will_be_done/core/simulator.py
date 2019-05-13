from decimal import *
from random import randrange

from ciscox83.global_properties import MONTECARLO_ITERATIONS
from ciscox83.when_it_will_be_done.core.constants import WORKING_DAYS_IN_ITERATION


class Simulator:
    def __init__(self, iterations):
        self.iterations = iterations
        self.past_cycle_times = self.__past_cycle_times()
        pass

    def __past_cycle_times(self):
        cycle_times = []
        for iteration in self.iterations:
            completed_iteration = iteration.get_completed()
            if completed_iteration > 0:
                cycle_time = WORKING_DAYS_IN_ITERATION / iteration.get_completed()
            else:
                cycle_time = 0
            cycle_times.append(Decimal(cycle_time).__round__(2))
        return cycle_times

    #
    # Uses Montecarlo simulation technique to generate a set of (possible)
    # number of iterations needed to complete the Epic
    #
    def simulate(self, pending_items):
        simulated_iterations_length = []
        number_of_past_cycle_times = len(self.past_cycle_times)
        for x in range(0, MONTECARLO_ITERATIONS, 1):
            total_days = 0
            for y in range(0, number_of_past_cycle_times, 1):
                i = randrange(number_of_past_cycle_times)
                total_days = total_days + self.past_cycle_times[i]
            average_cycle_time = total_days / number_of_past_cycle_times
            iteration_length = round(pending_items * average_cycle_time / WORKING_DAYS_IN_ITERATION)
            simulated_iterations_length.append(iteration_length)
        return simulated_iterations_length