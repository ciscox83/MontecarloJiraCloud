import unittest
from unittest.mock import Mock

from ciscox83.montecarlo.core.date_manager import DateManager
from ciscox83.montecarlo.core.jira_cloud_service import JiraCloudService


class MontecarloUnitTest(unittest.TestCase):
    date_manager = DateManager()

    def test_that_end_of_iteration_boundary_include_whole_day(self):
        date = self.date_manager.adjust_iteration_end_date("27/12/2018")
        self.assertEqual("2018/12/27 23:59", date)

    def test_that_raise_an_error_if_input_format_not_match(self):
        self.assertRaises(ValueError, self.date_manager.adjust_iteration_end_date, "2018-12-27")

    def test_that_can_get_start_of_iteration_boundary(self):
        a_week_ago = self.date_manager.get_iteration_start_date('27/12/2018')
        self.assertEqual("2018/12/20 00:00", a_week_ago)

    def test_that_can_retrieve_number_of_items_completed_in_last_n_iteration(self):
        jira_cloud_dao_mock = Mock()
        jira_cloud_service = JiraCloudService(jira_cloud_dao_mock)
        jira_cloud_dao_mock.get_number_of_completed_items_in_iteration.side_effect = [9, 8, 7]

        epic = "MOCK_EPIC"
        last_iteration_end_date = "MOCK_DATE"
        number_of_past_iterations = 3
        data = jira_cloud_service.get_number_of_completed_items_in_last_n_iterations(
            last_iteration_end_date,
            epic,
            number_of_past_iterations)
        for i in range(1, len(data) + 1, 1):
            print(str(data[i]) + " item(s) completed" \
                  + " in the iteration " + str(i) \
                  + " up to " + last_iteration_end_date + " on the epic " + epic)
            self.assertEqual(data[i], 6 + i)
if __name__ == '__main__':
    unittest.main()
