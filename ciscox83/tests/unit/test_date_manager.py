import unittest

from ciscox83.when_it_will_be_done.core.date_manager import DateManager

class DateManagerUnitTest(unittest.TestCase):
    date_manager = DateManager()

    def test_that_end_of_iteration_boundary_include_whole_day(self):
        date = self.date_manager.adjust_iteration_end_date("2018/12/27")
        self.assertEqual("2018/12/27 23:59", date)

    def test_that_raise_an_error_if_input_format_not_match(self):
        self.assertRaises(ValueError, self.date_manager.adjust_iteration_end_date, "2018-12-27")

    def test_that_can_get_start_of_iteration_boundary(self):
        a_week_ago = self.date_manager.get_iteration_start_date("2018/12/27")
        self.assertEqual("2018/12/20 00:00", a_week_ago)

    def test_that_can_convert_duration_into_date(self):
        duration = 7.2
        today = "2019/05/08"
        end_date = self.date_manager.get_project_end_date(duration, today)
        expected_end_date = "2019/06/27"
        self.assertEqual(expected_end_date, end_date)


if __name__ == '__main__':
    unittest.main()
