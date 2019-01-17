import unittest
from decimal import *

from ciscox83.montecarlo.core.iterations import Iteration
from ciscox83.montecarlo.core.montecarlo import Montecarlo


class MontecarloUnitTest(unittest.TestCase):

    def test_that_can_get_real_cycle_times(self):
        iterations = [
            Iteration(7, "2018/12/08 00:00", "2018/12/15 23:59"),
            Iteration(8, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(9, "2018/12/21 00:00", "2018/12/28 23:59")
        ]

        montecarlo = Montecarlo(iterations)
        cycle_times = montecarlo.get_real_cycle_times()
        self.assertEqual(cycle_times,
                         [Decimal(0.71).__round__(2),
                          Decimal(0.62).__round__(2),
                          Decimal(0.56).__round__(2)])


if __name__ == '__main__':
    unittest.main()
