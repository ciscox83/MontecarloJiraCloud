import unittest
from unittest.mock import Mock

from ciscox83.when_it_will_be_done.core.iteration import Iteration
from ciscox83.when_it_will_be_done.core.jira_cloud_service import JiraCloudService

class JiraCloudServiceUnitTest(unittest.TestCase):

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


        jira_cloud_dao_mock.get_iteration.side_effect = [
            Iteration(9, "2018/12/21 00:00", "2018/12/28 23:59"),
            Iteration(0, "2018/12/15 00:00", "2018/12/21 23:59"),
            Iteration(8, "2018/12/08 00:00", "2018/12/15 23:59")
            ]

        iterations = jira_cloud_service.get_iterations(
            last_iteration_end_date,
            epic,
            number_of_past_iterations)

        for i, iteration in enumerate(iterations):
            if i == 0:
                self.assertEqual(iteration.get_completed(), 8)
                self.assertEqual(iteration.get_start_date(), "2018/12/08 00:00")
                self.assertEqual(iteration.get_end_date(), "2018/12/15 23:59")
            if i == 1:
                self.assertEqual(iteration.get_completed(), 9)
                self.assertEqual(iteration.get_start_date(), "2018/12/21 00:00")
                self.assertEqual(iteration.get_end_date(), "2018/12/28 23:59")


if __name__ == '__main__':
    unittest.main()
