"""

"""

import numpy as np
from scipy import stats


SLOPE_SCORE_MAP = {
    25: (0.01, 0.25),
    50: (0.26, 0.50),
    75: (0.51, 0.75),
    100: (0.75, 100000)
}


def search(values, search_for):
    """

    :param values:
    :param search_for:
    :return:
    """

    # If search value is 0 or less then return 0
    if search_for <= 0:
        return 0

    for k in values:
        if values[k][0] <= search_for <= values[k][1]:
            return int(k)

    return None


def get_slope_score(slope_score):
    """

    :param slope_score:
    :return:
    """

    return search(SLOPE_SCORE_MAP, slope_score)


# TODO: Need to clear manual slope calculation if python scipy stats.linregress works as expected
'''
def simple_linear_regression(input_x, y):
    """
    Returns slope and intercept for a simple regression line

    inputs- Works best with numpy arrays, though other similar data structures will work fine.
        input_x - input data
        y - output data

    :param input_x:
    :param y:
    :return: floats
    """

    # initial sums
    n = float(len(input_x))

    sum_x = input_x.sum()
    sum_y = y.sum()

    sum_xy = (input_x * y).sum()
    sum_xx = (input_x ** 2).sum()

    # formula for w0
    slope = (sum_xy - (sum_x * sum_y) / n) / (sum_xx - (sum_x * sum_x) / n)

    # formula for w1
    intercept = sum_y / n - slope * (sum_x / n)

    return intercept, slope
'''


def trajectory_score(known_y, known_x):
    """
    :param known_y:
    :param known_x:
    :return:
    """

    x = np.array(known_x)
    y = np.array(known_y)

    # If date and visit array content single record then return 0 score
    if 1 in (len(x), len(y)):
        return 0

    # Manual calculation
    # intercept, slope = simple_linear_regression(y, x)

    # scipy stats linregress
    slope, intercept, r_value, p_value, std_err = stats.linregress(y, x)

    #print slope
    slope_score = round(slope, 2)

    return get_slope_score(slope_score)
