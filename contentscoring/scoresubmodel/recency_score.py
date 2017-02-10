"""
This is recency sub score model
"""

RECENCY_SCORE_MAP = {
    'week_4': 40,
    'week_3': 30,
    'week_2': 20,
    'week_1': 10
}


def get_recency_score(aggregated_score, score_index):
    """

    :param aggregated_score:
    :param score_index:
    :return:
    """

    return RECENCY_SCORE_MAP[score_index] if aggregated_score[1] >= 1 else 0


def get_sumtotal_aggregate_score(week_data, divisor):
    """

    :param week_data:
    :param divisor:
    :return:
    """
    return week_data[1]/divisor


def recency_score(date_range, visit_range, base_divisor, time_range):
    """

    :param date_range:
    :param visit_range:
    :param base_divisor:
    :param time_range:
    :return:
    """

    r_score = 0

    aggregated_score_by_week = []

    """
    Calculate divisor Here are the criteria

    if time_range is 1 then
        divisor = base_divisor * time_range i.e 5 * 1 == 5
    else if time_range == 3 then
        divisor = base_divisor * time_range i.e 5 * 3 == 15
    else if time_range == 6 then
        divisor = base_divisor * time_range i.e 5 * 6 == 30
    else if time_range == 13 then
        divisor = base_divisor * time_range i.e 5 * 13 == 65
    """

    divisor = time_range * base_divisor

    # zip data with weeks
    club_data = zip(date_range, visit_range)

    # Get aggregate score divided by time range divisor
    for data_ele in club_data:

        aggregated_score = get_sumtotal_aggregate_score(data_ele, divisor)

        aggregated_score_by_week.append((data_ele[0], aggregated_score))

    # Get recency score and sum total score
    for week_idx, aggregated_score in enumerate(aggregated_score_by_week):

        week_score_idx = 'week_{0}'.format(week_idx+1)

        r_score += get_recency_score(aggregated_score, week_score_idx)

    return r_score
