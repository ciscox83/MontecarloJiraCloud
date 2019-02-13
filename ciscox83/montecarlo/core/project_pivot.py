from ciscox83.montecarlo.core.project_pivot_entry import ProjectPivotEntry



class ProjectPivot:
    def __init__(self, simulated_iterations):
        self.simulated_iterations = simulated_iterations
        self.pivots = self.__compute_project_pivots(simulated_iterations)
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

    def normalise(self, cumulative_percentages):
        max_number_of_occurrences = self.get_max_number_of_occurrences(self.simulated_iterations)
        normalised_cumulative_percentages = []
        for i in range (0, len(cumulative_percentages), 1):
            normalised_cumulative_percentages.append(round(max_number_of_occurrences / 100 * cumulative_percentages[i], 1))
        return normalised_cumulative_percentages

    @staticmethod
    def get_max_number_of_occurrences(iterations):
        max_number_of_occurrences = 0
        for percentage in iterations:
            count = iterations.count(percentage)
            if count > max_number_of_occurrences:
                max_number_of_occurrences = count
        return max_number_of_occurrences