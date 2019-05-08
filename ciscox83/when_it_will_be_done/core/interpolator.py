from scipy.interpolate import interp1d

class Interpolator:
    def __init__(self):
        pass

    def approximate_forecasted_duration(self, cumulative_percentages, iteration_lenghts, target_cumulative_percentage):
        x = cumulative_percentages
        y = iteration_lenghts
        f = interp1d(x, y, kind='cubic')
        return round(f(target_cumulative_percentage).item(0), 1)