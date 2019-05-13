import unittest
from decimal import *

from ciscox83.global_properties import MONTECARLO_ITERATIONS
from ciscox83.when_it_will_be_done.core.iteration import Iteration
from ciscox83.when_it_will_be_done.core.simulator import Simulator


class SimulatorUnitTest(unittest.TestCase):

    def test_that_can_compute_past_cycle_times(self):
        iterations = [
            Iteration(7, "2018/12/08 00:00", "2018/12/15 23:59"),
            Iteration(8, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(9, "2018/12/21 00:00", "2018/12/28 23:59")
        ]

        simulator = Simulator(iterations)
        cycle_times = simulator.past_cycle_times
        self.assertEqual(cycle_times,
                         [Decimal(0.71).__round__(2),
                          Decimal(0.62).__round__(2),
                          Decimal(0.56).__round__(2)])

    def test_that_can_compute_past_cycle_times_with_zero_items_completed(self):
        iterations = [
            Iteration(7, "2018/12/08 00:00", "2018/12/15 23:59"),
            Iteration(0, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(9, "2018/12/21 00:00", "2018/12/28 23:59")
        ]

        simulator = Simulator(iterations)
        cycle_times = simulator.past_cycle_times
        self.assertEqual(cycle_times,
                         [Decimal(0.71).__round__(2),
                          Decimal(0.0).__round__(2),
                          Decimal(0.56).__round__(2)])

    def test_that_can_compute_simulated_iterations(self):
        items_completed_in_iteration = 7
        pending_items = 7
        past_iterations = [
            Iteration(items_completed_in_iteration, "2018/12/08 00:00", "2018/12/15 23:59"),
            Iteration(items_completed_in_iteration, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(items_completed_in_iteration, "2018/12/21 00:00", "2018/12/28 23:59")
        ]

        simulator = Simulator(past_iterations)
        simulated_iterations_length = simulator.simulate(pending_items)
        num_of_simulated_iterations = len(simulated_iterations_length)
        self.assertEqual(num_of_simulated_iterations, MONTECARLO_ITERATIONS)
        for i in range(0, num_of_simulated_iterations, 1):
            self.assertEqual(simulated_iterations_length[i], pending_items / items_completed_in_iteration)


    def test_that_can_compute_simulated_iterations_when_are_missing_few_items(self):
        items_completed_in_iteration = 7
        pending_items = 1
        past_iterations = [
            Iteration(items_completed_in_iteration, "2018/12/08 00:00", "2018/12/15 23:59"),
            Iteration(items_completed_in_iteration, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(items_completed_in_iteration, "2018/12/21 00:00", "2018/12/28 23:59")
        ]

        simulator = Simulator(past_iterations)
        simulated_iterations_length = simulator.simulate(pending_items)
        num_of_simulated_iterations = len(simulated_iterations_length)
        self.assertEqual(num_of_simulated_iterations, MONTECARLO_ITERATIONS)
        expected_simulated_iteration_length = Decimal('0.1')
        for i in range(0, num_of_simulated_iterations, 1):
            self.assertEqual(simulated_iterations_length[i], expected_simulated_iteration_length)





if __name__ == '__main__':
    unittest.main()
