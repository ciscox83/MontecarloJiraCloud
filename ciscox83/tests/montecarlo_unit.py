import unittest
from decimal import *
from unittest.mock import Mock

from ciscox83.montecarlo.core.date_manager import DateManager
from ciscox83.montecarlo.core.iterations import Iteration
from ciscox83.montecarlo.core.jira_cloud_service import JiraCloudService
from ciscox83.montecarlo.core.montecarlo import Montecarlo


class MontecarloUnitTest(unittest.TestCase):
    date_manager = DateManager()

    def test_that_end_of_iteration_boundary_include_whole_day(self):
        date = self.date_manager.adjust_iteration_end_date("2018/12/27")
        self.assertEqual("2018/12/27 23:59", date)

    def test_that_raise_an_error_if_input_format_not_match(self):
        self.assertRaises(ValueError, self.date_manager.adjust_iteration_end_date, "2018-12-27")

    def test_that_can_get_start_of_iteration_boundary(self):
        a_week_ago = self.date_manager.get_iteration_start_date("2018/12/27")
        self.assertEqual("2018/12/20 00:00", a_week_ago)

    def test_that_can_retrieve_number_of_items_completed_in_last_n_iterations(self):
        jira_cloud_dao_mock = Mock()
        jira_cloud_service = JiraCloudService(jira_cloud_dao_mock)
        jira_cloud_dao_mock.get_iteration.side_effect = [
            Iteration(9, "2018/12/21 00:00", "2018/12/28 23:59"),
            Iteration(8, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(7, "2018/12/08 00:00", "2018/12/15 23:59")
            ]

        epic = "SOME_EPIC"
        last_iteration_end_date = "2018/12/28"
        number_of_past_iterations = 3
        iterations = jira_cloud_service.get_iterations(
            last_iteration_end_date,
            epic,
            number_of_past_iterations)

        for i, iteration in enumerate(iterations):
            if i == 0:
                self.assertEqual(iteration.get_completed(), 7)
                self.assertEqual(iteration.get_start_date(), "2018/12/08 00:00")
                self.assertEqual(iteration.get_end_date(), "2018/12/15 23:59")
            if i == 1:
                self.assertEqual(iteration.get_completed(), 8)
                self.assertEqual(iteration.get_start_date(), "2018/12/15 00:00")
                self.assertEqual(iteration.get_end_date(), "2018/12/21 23:59")
            if i == 2:
                self.assertEqual(iteration.get_completed(), 9)
                self.assertEqual(iteration.get_start_date(), "2018/12/21 00:00")
                self.assertEqual(iteration.get_end_date(), "2018/12/28 23:59")

    def test_that_iteration_outcome_is_normalised(self):
        jira_cloud_dao_mock = Mock()
        jira_cloud_service = JiraCloudService(jira_cloud_dao_mock)
        jira_cloud_dao_mock.get_iteration.side_effect = [
            Iteration(9, "2018/12/21 00:00", "2018/12/28 23:59"),
            Iteration(8, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(0, "2018/12/08 00:00", "2018/12/15 23:59")
            ]

        epic = "SOME_EPIC"
        last_iteration_end_date = "2018/12/28"
        number_of_past_iterations = 3
        iterations = jira_cloud_service.get_iterations(
            last_iteration_end_date,
            epic,
            number_of_past_iterations)

        expected_iterations = 2
        actual_iterations = len(iterations)
        self.assertEqual(expected_iterations, actual_iterations)
        for i, iteration in enumerate(iterations):
            if i == 0:
                self.assertEqual(iteration.get_completed(), 8)
                self.assertEqual(iteration.get_start_date(), "2018/12/15 00:00")
                self.assertEqual(iteration.get_end_date(), "2018/12/21 23:59")
            if i == 1:
                self.assertEqual(iteration.get_completed(), 9)
                self.assertEqual(iteration.get_start_date(), "2018/12/21 00:00")
                self.assertEqual(iteration.get_end_date(), "2018/12/28 23:59")

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
