"""
This is completion sub score model
"""


def get_completion_score(downloads_count, visits_count):
    """

    :param downloads_count:
    :param visits_count:
    :return:
    """

    c_score = int((float(downloads_count) / float(visits_count)) * 100)

    if c_score > 100:

        return 100

    return c_score


def completion_score(file_downloads_count, web_visits_by_week):
    """

    :param file_downloads_count:
    :param web_visits_by_week:
    :return:
    """

    return get_completion_score(file_downloads_count, web_visits_by_week)
