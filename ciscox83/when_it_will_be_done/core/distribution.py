class Distribution:
    def __init__(self, simulated_iteration_lengths):
        self.simulated_iteration_lengths = simulated_iteration_lengths
        self.unique_simulated_iteration_lengths = sorted(list(dict.fromkeys(simulated_iteration_lengths)))
        pass

    def get_unique_simulated_iteration_lengths(self):
        return self.unique_simulated_iteration_lengths

    def get_cumulative_percentages(self):
        cumulative_percentages = []
        cumulative_percentage = 0
        for iteration_length in self.unique_simulated_iteration_lengths:
            count = self.simulated_iteration_lengths.count(iteration_length)
            percentage = round(count * 100 / len(self.simulated_iteration_lengths), 0)
            cumulative_percentage = cumulative_percentage + percentage
            cumulative_percentages.append(cumulative_percentage)
        return cumulative_percentages