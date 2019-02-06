from ciscox83.montecarlo.core.project_pivot_entry import ProjectPivotEntry


class ProjectPivot:
    def __init__(self, simulated_durations):
        self.pivots = self.__compute_project_pivots(simulated_durations)
        pass

    @staticmethod
    def __compute_project_pivots(simulated_durations):
        unique_simulated_durations = set(simulated_durations)

        computed_pivots = []
        for duration in unique_simulated_durations:
            count = simulated_durations.count(duration)
            percentage = round(count * 100 / len(simulated_durations), 0)
            computed_pivots.append(ProjectPivotEntry(duration, count, percentage))

        return computed_pivots

    def get_pivots(self):
        return self.pivots

    def get_cumulative_percentages(self):
        cumulative_percentages = [self.pivots[0].get_percentage()]
        for i in range(1, len(self.pivots), 1):
            prev_percentage = cumulative_percentages[i - 1]
            current_percentage = self.pivots[i].get_percentage()
            cumulative_percentages.append(prev_percentage + current_percentage)
        return cumulative_percentages