import logging
import requests
import properties


class JiraCloudService:
    logger = logging.getLogger()

    def __init__(self):
        self.url = "https://" \
              + properties.account \
              + ".atlassian.net/rest/api/" \
              + properties.jira_api_version \
              + "/project/" \
              + properties.my_jira_project

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": properties.my_jira_auth
        }

    def get_my_project(self):
        return requests.request(
            "GET",
            self.url,
            headers=self.headers
        )
