import requests
import json
import ciscox83.user_properties as user_properties
import ciscox83.global_properties as properties
from ciscox83.when_it_will_be_done.core.date_manager import DateManager
from ciscox83.when_it_will_be_done.core.iteration import Iteration


class JiraCloudDao:

    def __init__(self):
        self.url = "https://" \
                   + user_properties.my_jira_account \
                   + ".atlassian.net/rest/api/" \
                   + properties.JIRA_API_VERSION

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic " + user_properties.my_jira_auth_token
        }

    def get_my_project(self):
        url = self.url \
              + "/project/" \
              + user_properties.my_jira_project
        return requests.request(
            "GET",
            url,
            headers=self.headers
        )

    def get_iteration(self, date_end, epic_link):
        iteration_start_date = DateManager.get_iteration_start_date(date_end)
        iteration_end_date = DateManager.adjust_iteration_end_date(date_end)
        url = self.url \
              + "/search/" \
              + "?jql=" \
              + "project = " + user_properties.my_jira_project \
              + " AND status = Done" \
              + " AND updated >= " + "\"" + iteration_start_date + "\"" \
              + " AND updated <= " + "\"" + iteration_end_date + "\"" \
              + " AND \"Epic Link\" = " + epic_link
        response = requests.request(
            "GET",
            url,
            headers=self.headers
        )
        response_data = json.loads(response.text)
        return Iteration(len(response_data['issues']), iteration_start_date, iteration_end_date)

    #
    # Used for integration tests purposes
    #
    def get_random_epic_key(self):
        url = self.url \
              + "/search/" \
              + "?jql=" \
              + "project = " + user_properties.my_jira_project \
              + " AND issuetype = Epic"
        response = requests.request(
            "GET",
            url,
            headers=self.headers
        )
        return json.loads(response.text)['issues'][0]['key']