class Distribution:
    def __init__(self):
        pass

    @staticmethod
    def get_unique_simulated_iteration_lenghts(simulated_iteration_lengths):
        return sorted(list(dict.fromkeys(simulated_iteration_lengths)))

    def get_cumulative_percentages(self, simulated_iteration_lengths):
        unique_simulated_iteration_lengths = self.get_unique_simulated_iteration_lenghts(simulated_iteration_lengths)
        cumulative_percentages = []
        cumulative_percentage = 0
        for iteration_length in unique_simulated_iteration_lengths:
            count = simulated_iteration_lengths.count(iteration_length)
            percentage = round(count * 100 / len(simulated_iteration_lengths), 0)
            cumulative_percentage = cumulative_percentage + percentage
            cumulative_percentages.append(cumulative_percentage)
        return cumulative_percentages