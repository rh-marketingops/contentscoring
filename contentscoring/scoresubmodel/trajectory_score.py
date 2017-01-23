"""

"""

import numpy as np
from scipy import stats


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


def get_slope_score(trajectory_score):
    """

    :param trajectory_score:
    :return:
    """

    slope_score = {

        25: (0.01, 0.25),
        50: (0.26, 0.50),
        75: (0.51, 0.75),
        100: (0.75,100000)
    }

    return search(slope_score, trajectory_score)


def simple_linear_regression(X, y):
    """
    Returns slope and intercept for a simple regression line

    inputs- Works best with numpy arrays, though other similar data structures will work fine.
        X - input data
        y - output data

    :param X:
    :param y:
    :return: floats
    """

    # initial sums
    n = float(len(X))

    sum_x = X.sum()
    sum_y = y.sum()

    sum_xy = (X * y).sum()
    sum_xx = (X ** 2).sum()

    # formula for w0
    slope = (sum_xy - (sum_x * sum_y) / n) / (sum_xx - (sum_x * sum_x) / n)

    # formula for w1
    intercept = sum_y / n - slope * (sum_x / n)

    return (intercept, slope)


def trajectory_score(known_y, known_x):
    """
    :param data:
    :param db:
    :param config_name:
    :param config:
    :return:
    """

    x = np.array(known_x)
    y = np.array(known_y)

    if 1 in (len(x), len(y)):
        return 0

    # Manual calculation
    # intercept, slope = simple_linear_regression(y, x)

    # scipy stats linregress
    slope, intercept, r_value, p_value, std_err = stats.linregress(y, x)

    print slope

    t_score = round(slope, 2)

    return get_slope_score(t_score)
