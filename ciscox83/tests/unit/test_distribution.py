import unittest

from ciscox83.when_it_will_be_done.core.distribution import Distribution

class DistributionUnitTest(unittest.TestCase):

    def test_that_can_get_unique_iteration_lengths(self):
        simulated_iteration_lengths = [4, 2, 3, 3, 3, 1, 1]
        distribution = Distribution(simulated_iteration_lengths)
        expected_unique_simulated_iteration_lengths = [1, 2, 3, 4]
        unique_simulated_iteration_lengths = distribution.get_unique_simulated_iteration_lengths()
        for i in (0, 3):
            self.assertEqual(expected_unique_simulated_iteration_lengths[i], unique_simulated_iteration_lengths[i])

    def test_that_can_get_cumulative_percentages(self):
        simulated_iteration_lengths = [4, 2, 3, 3, 3, 1, 1]
        distribution = Distribution(simulated_iteration_lengths)
        expected_cumulative_percentages = [29, 43, 86, 100]

        cumulative_percentages = distribution.get_cumulative_percentages(simulated_iteration_lengths)

        for i in (0, 3):
            self.assertEqual(expected_cumulative_percentages[i], cumulative_percentages[i])


if __name__ == '__main__':
    unittest.main()