from ciscox83.when_it_will_be_done.core.date_manager import DateManager

class JiraCloudService:
    def __init__(self, jira_cloud_dao):
        self.data = []
        self.jira_cloud_dao = jira_cloud_dao

    def get_iterations(self, last_iteration_end_date, epic_link, number_of_iterations):
        iterations = []
        for i in range(0, number_of_iterations):
            iterations.append(self.jira_cloud_dao.get_iteration(last_iteration_end_date, epic_link))
            last_iteration_end_date = DateManager.get_iteration_start_date(last_iteration_end_date)
        return self.__normalise(iterations)


    # Remove the iterations with no delivery considering them exceptions (holidays, etc.)
    @staticmethod
    def __normalise(iterations):
        iterations.reverse()

        for i, iteration in enumerate(iterations):
            if iteration.get_completed() == 0:
                iterations.pop(i)
        return iterations
