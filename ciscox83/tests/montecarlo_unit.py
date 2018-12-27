import unittest
from ciscox83.montecarlo.core.datemanager import DateManager


class MontecarloUnitTest(unittest.TestCase):
    date_manager = DateManager()

    def test_can_get_a_week_ago_date(self):
        today = "2018/12/27"
        a_week_ago = self.date_manager.a_week_ago(today)
        self.assertEqual("2018/12/20 00:00", a_week_ago)


if __name__ == '__main__':
    unittest.main()
