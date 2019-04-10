import unittest
from decimal import *

from ciscox83.global_properties import MONTECARLO_ITERATIONS
from ciscox83.montecarlo.core.iteration import Iteration
from ciscox83.montecarlo.core.epic_simulation import EpicSimulator


class MontecarloUnitTest(unittest.TestCase):

    def test_that_can_compute_past_cycle_times(self):
        iterations = [
            Iteration(7, "2018/12/08 00:00", "2018/12/15 23:59"),
            Iteration(8, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(9, "2018/12/21 00:00", "2018/12/28 23:59")
        ]

        epic_simulator = EpicSimulator(iterations)
        cycle_times = epic_simulator.past_cycle_times
        self.assertEqual(cycle_times,
                         [Decimal(0.71).__round__(2),
                          Decimal(0.62).__round__(2),
                          Decimal(0.56).__round__(2)])

    def test_that_can_compute_simulated_iterations(self):
        items_completed_in_iteration = 7
        pending_items = 21
        past_iterations = [
            Iteration(items_completed_in_iteration, "2018/12/08 00:00", "2018/12/15 23:59"),
            Iteration(items_completed_in_iteration, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(items_completed_in_iteration, "2018/12/21 00:00", "2018/12/28 23:59")
        ]

        epic_simulator = EpicSimulator(past_iterations)
        simulated_iterations_length = epic_simulator.simulate(pending_items)
        num_of_simulated_iterations = len(simulated_iterations_length)
        self.assertEqual(num_of_simulated_iterations, MONTECARLO_ITERATIONS)
        for i in range(0, num_of_simulated_iterations, 1):
            self.assertEqual(simulated_iterations_length[i], pending_items / items_completed_in_iteration)





if __name__ == '__main__':
    unittest.main()
