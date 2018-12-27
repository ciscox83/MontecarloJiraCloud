import unittest
from ciscox83.montecarlo.core.date_manager import DateManager


class MontecarloUnitTest(unittest.TestCase):
    date_manager = DateManager()

    def test_that_end_of_iteration_boundary_include_whole_day(self):
        self.assertEqual("2018/12/27 23:59:59", self.date_manager.iteration_end_date("2018/12/27"))

    def test_that_raise_an_error_if_input_format_not_match(self):
        self.assertRaises(ValueError, self.date_manager.iteration_end_date, "2018-12-27")

    def test_can_get_a_week_ago_date_in_jira_format(self):
        today = "2018/12/27"
        a_week_ago = self.date_manager.iteration_start_date(today)
        self.assertEqual("2018/12/20 00:00", a_week_ago)


if __name__ == '__main__':
    unittest.main()
