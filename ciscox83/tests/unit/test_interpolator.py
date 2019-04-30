import unittest

from ciscox83.when_it_will_be_done.core.distribution_entry import DistributionEntry
from ciscox83.when_it_will_be_done.core.interpolator import Interpolator


class InterpolatorUnitTest(unittest.TestCase):

    def test_that_can_infer_forecasted_iteration_length(self):
        entry1 = DistributionEntry(4, 14)
        entry2 = DistributionEntry(5, 33)
        entry3 = DistributionEntry(6, 58)
        entry4 = DistributionEntry(7, 77)
        entry5 = DistributionEntry(8, 90)
        entry6 = DistributionEntry(9, 96)
        entry7 = DistributionEntry(10, 100)

        iteration_length_to_cumulative_percentages = [entry1, entry2, entry3, entry4, entry5, entry6, entry7]

        desired_cumulative_percentage = 80
        expected_interpolated_iteration_length = 7.2

        interpolator = Interpolator()
        interpolated_iteration_length = interpolator.quadratic_interpolation(
            iteration_length_to_cumulative_percentages, desired_cumulative_percentage)

        self.assertEqual(expected_interpolated_iteration_length, interpolated_iteration_length)


if __name__ == '__main__':
    unittest.main()