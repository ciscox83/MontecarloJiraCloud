import unittest

from ciscox83.when_it_will_be_done.core.interpolator import Interpolator


class InterpolatorUnitTest(unittest.TestCase):

    def test_that_can_infer_forecasted_iteration_length(self):
        cumulative_percentages = [14, 33, 58, 77, 90, 96, 100]
        iteration_lenghts = [4, 5, 6, 7, 8, 9, 10]

        target_cumulative_percentage = 80
        expected_interpolated_iteration_length = 7.2

        interpolator = Interpolator()
        interpolated_iteration_length = interpolator.approximate_forecasted_duration(
            cumulative_percentages, iteration_lenghts, target_cumulative_percentage)

        self.assertEqual(expected_interpolated_iteration_length, interpolated_iteration_length)


if __name__ == '__main__':
    unittest.main()