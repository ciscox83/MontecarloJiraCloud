import unittest

from ciscox83.montecarlo.core.project_pivot import ProjectPivot

class ProjectPivotUnitTest(unittest.TestCase):

    def test_that_pivot_order_is_correct(self):
        simulated_iterations = [4, 2, 3, 3, 3, 1, 1]
        project_pivot = ProjectPivot(simulated_iterations)

        expected_durations = [1, 2, 3, 4]
        expected_count = [2, 3, 1, 1]
        expected_percentages = [29, 14, 43, 14]

        pivots = project_pivot.get_pivots()

        for i in (0, 3):
            self.assertEqual(pivots[i].get_duration(), expected_durations[i])
            self.assertEqual(pivots[i].get_count(), expected_count[i])
            self.assertEqual(pivots[i].get_percentage(), expected_percentages[i])

    def test_can_compute_cumulative_percentage(self):
        simulated_iterations = [4, 2, 3, 3, 3, 1, 1]
        project_pivot = ProjectPivot(simulated_iterations)
        cumulative_percentages = project_pivot.get_cumulative_percentages()

        expected_cumulative_percentages = [29, 43, 86, 100]
        self.assertEqual(cumulative_percentages, expected_cumulative_percentages)

    def test_can_normalise_cumulative_percentages(self):
        simulated_iterations = [4, 2, 3, 3, 3, 1, 1]
        project_pivot = ProjectPivot(simulated_iterations)

        cumulative_percentages = project_pivot.get_cumulative_percentages()
        expected_normalisation = [0.87, 1.29, 2.58, 3.0]
        actual_normalisations = project_pivot.normalise(cumulative_percentages)

        for i in range(0, len(actual_normalisations) - 1):
            self.assertEqual(actual_normalisations[i], expected_normalisation[i])

if __name__ == '__main__':
    unittest.main()