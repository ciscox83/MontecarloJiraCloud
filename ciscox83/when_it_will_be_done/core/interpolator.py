from scipy.interpolate import interp1d

class Interpolator:
    def __init__(self):
        pass

    @staticmethod
    def approximate_forecasted_duration(cumulative_percentages, iteration_lengths, target_cumulative_percentage):
        x = cumulative_percentages
        y = iteration_lengths

        i = x[0]
        x_no_duplicates = [i]
        y_no_duplicates = [y[0]]
        for j in range(1, len(x)):
            if i != x[j]:
                x_no_duplicates.append(x[j])
                y_no_duplicates.append(y[j])
            i = x[j]

        f = interp1d(x_no_duplicates, y_no_duplicates, kind='cubic')
        return round(f(target_cumulative_percentage).item(0), 1)