import unittest

from ciscox83.when_it_will_be_done.core.distribution import Distribution

class DistributionUnitTest(unittest.TestCase):

    def test_that_distribution_order_is_correct(self):
        simulated_iteration_lengths = [4, 2, 3, 3, 3, 1, 1]
        distribution = Distribution()
        iteration_length_to_cumulative_percentages = distribution.iteration_length_to_cumulative_percentages(simulated_iteration_lengths)

        expected_durations = [1, 2, 3, 4]
        expected_cumulative_percentages = [29, 43, 86, 100]

        for i in (0, 3):
            self.assertEqual(iteration_length_to_cumulative_percentages[i].get_duration(), expected_durations[i])
            self.assertEqual(iteration_length_to_cumulative_percentages[i].get_cumulative_percentage(), expected_cumulative_percentages[i])

if __name__ == '__main__':
    unittest.main()