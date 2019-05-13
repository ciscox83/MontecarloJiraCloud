from scipy.interpolate import interp1d

class Interpolator:
    def __init__(self):
        pass

    @staticmethod
    def approximate_forecasted_duration(cumulative_percentages, iteration_lengths, target_cumulative_percentage):
        x = cumulative_percentages
        y = iteration_lengths
        f = interp1d(x, y, kind='cubic')
        return round(f(target_cumulative_percentage).item(0), 1)