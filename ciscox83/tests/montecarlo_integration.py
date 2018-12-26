import unittest
from ciscox83.montecarlo.core import jira_cloud_service


class MontecarloIntegrationTest(unittest.TestCase):
    jira = jira_cloud_service.JiraCloudService()

    def test_can_connect_with_jira_cloud(self):
        response = self.jira.get_my_project()

        # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
