import logging
import requests
import json
import ciscox83.user_properties as user_properties
import ciscox83.global_properties as properties
from ciscox83.montecarlo.core.date_manager import DateManager


class JiraCloudService:
    logger = logging.getLogger()

    def __init__(self):
        self.url = "https://" \
                   + user_properties.my_jira_account \
                   + ".atlassian.net/rest/api/" \
                   + properties.jira_api_version

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

    def get_number_of_completed_items_in_iteration(self, date_end, epic_link):
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
        data = json.loads(response.text)
        return len(data['issues'])

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
