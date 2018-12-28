class JiraCloudService:
    def __init__(self, jira_cloud_dao):
        self.data = []
        self.jira_cloud_dao = jira_cloud_dao

    def get_number_of_completed_items_in_last_n_iterations(self, last_iteration_end_date, epic, number_of_iterations):
        data = {}
        for i in range(number_of_iterations, 0, -1):
            number = self.jira_cloud_dao.get_number_of_completed_items_in_iteration(last_iteration_end_date, epic)
            data[i] = number
        return data