from ciscox83.when_it_will_be_done.core.distribution_entry import DistributionEntry



class Distribution:
    def __init__(self):
        pass

    @staticmethod
    def iteration_length_to_cumulative_percentages(simulated_iteration_lengths):
        unique_simulated_iteration_lengths = set(simulated_iteration_lengths)

        iteration_length_to_cumulative_percentages = []
        cumulative_percentage = 0
        for iteration_length in unique_simulated_iteration_lengths:
            count = simulated_iteration_lengths.count(iteration_length)
            percentage = round(count * 100 / len(simulated_iteration_lengths), 0)
            cumulative_percentage = cumulative_percentage + percentage
            iteration_length_to_cumulative_percentages.append(DistributionEntry(iteration_length, cumulative_percentage))

        return iteration_length_to_cumulative_percentages

    @staticmethod
    def get_unique_simulated_iteration_lenghts(simulated_iteration_lengths):
        return list(dict.fromkeys(simulated_iteration_lengths))