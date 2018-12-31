from ciscox83.montecarlo.core.date_manager import DateManager

class JiraCloudService:
    def __init__(self, jira_cloud_dao):
        self.data = []
        self.jira_cloud_dao = jira_cloud_dao

    def get_iterations(self, last_iteration_end_date, epic, number_of_iterations):
        iterations = {}
        for i in range(number_of_iterations, 0, -1):
            iterations[i] = self.jira_cloud_dao.get_iteration(last_iteration_end_date, epic)
            last_iteration_end_date = DateManager.get_iteration_start_date(last_iteration_end_date)
        return iterations