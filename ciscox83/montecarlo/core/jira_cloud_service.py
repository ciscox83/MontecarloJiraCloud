import logging
import requests
import ciscox83.user_properties as user_properties
import ciscox83.global_properties as properties


class JiraCloudService:
    logger = logging.getLogger()

    def __init__(self):
        self.url = "https://" \
                   + user_properties.my_jira_account \
              + ".atlassian.net/rest/api/" \
              + properties.jira_api_version \
              + "/project/" \
                   + user_properties.my_jira_project

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic " + user_properties.my_jira_auth_token
        }

    def get_my_project(self):
        return requests.request(
            "GET",
            self.url,
            headers=self.headers
        )
