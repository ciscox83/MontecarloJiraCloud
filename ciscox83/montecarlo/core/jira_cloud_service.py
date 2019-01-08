from ciscox83.montecarlo.core.date_manager import DateManager

class JiraCloudService:
    def __init__(self, jira_cloud_dao):
        self.data = []
        self.jira_cloud_dao = jira_cloud_dao

    def get_iterations(self, last_iteration_end_date, epic, number_of_iterations):
        iterations = []
        for i in range(0, number_of_iterations):
            iterations.append(self.jira_cloud_dao.get_iteration(last_iteration_end_date, epic))
            last_iteration_end_date = DateManager.get_iteration_start_date(last_iteration_end_date)
        return self.__normalise(iterations)


    def __normalise(self, iterations):
        iterations.reverse()
        return iterations
        # normalized_iterations = iterations.reverse()
        # i = 1
        # for iteration in iterations:
        #     if iteration.get_completed() == 0:
        #         del normalized_iterations[i]
        #         i = i + 1
        #     else:
        #         return normalized_iterations.reverse()