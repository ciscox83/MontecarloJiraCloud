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

if __name__ == '__main__':
    unittest.main()