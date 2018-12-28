import unittest
from datetime import datetime
from ciscox83.montecarlo.core import jira_cloud_dao


# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
class MontecarloIntegrationTest(unittest.TestCase):
    jira = jira_cloud_dao.JiraCloudDao()

    def test_can_retrieve_my_project(self):
        response = self.jira.get_my_project()
        self.assertEqual(response.status_code, 200)

    def test_that_can_retrieve_number_of_items_completed_in_last_iteration(self):
        epic = self.jira.get_random_epic_key()
        end_iteration_date = datetime.today().strftime("%d/%m/%Y")
        n = self.jira.get_number_of_completed_items_in_iteration(end_iteration_date, epic)
        print(str(n) + " item(s) completed in the last iteration up to " + end_iteration_date + " on the epic " + epic)
        self.assertGreaterEqual(n, 0,)

if __name__ == '__main__':
    unittest.main()
