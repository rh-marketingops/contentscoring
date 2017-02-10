"""
Un-gated content scoring model
"""

from contentscoring.scoresubmodel import completion_score
from contentscoring.scoresubmodel import recency_score
from contentscoring.scoresubmodel import trajectory_score

# from contentscoring.scoresubmodel import volume_score


def get_completion_score(asset_dict):
    """

    :param asset_dict:
    :return: Int completion score
    """

    return completion_score(asset_dict['file_download'], asset_dict['web_visits'])


def get_recency_score(asset_dict):
    """

    :param asset_dict:
    :return: Int recency score
    """

    return recency_score(asset_dict['week_date_range'],
                         asset_dict['week_visit_range'],
                         asset_dict['base_divisor'],
                         asset_dict['time_range'])


def get_trajectory_score(asset_dict):
    """

    :param asset_dict:
    :return: Int trajectory score
    """

    return trajectory_score(asset_dict['score_yrange'], asset_dict['score_xrange'])


def get_volume_score(asset_dict):
    """

    :param asset_dict:
    :return:
    """

    return trajectory_score(asset_dict['score_yrange'], asset_dict['score_xrange'])


def get_sub_score(asset_data_set):
    """

    :param asset_data_set:
    :return:
    """

    # return_score_dict = {}

    asset_score = {}

    for asset in asset_data_set:

        asset_score['completion_score'] = get_completion_score(asset_data_set[asset])
        asset_score['recency_score'] = get_recency_score(asset_data_set[asset])
        asset_score['trajectory_score'] = get_trajectory_score(asset_data_set[asset])

    return asset_score


def ungated_score(asset):
    """

    :return:
    """

    # Un-gated score for 1 month
    if not asset:
        raise("Asset should have downloaded, visited "
              "and weekly count for score calculation.")

    # Get completion score

    c_score = get_completion_score(asset)
    r_score = get_recency_score(asset)
    t_score = get_trajectory_score(asset)

    #v_score = get_volume_score()

    # un_gated_score = ((completion_score * 0.35)
    # + (recency_score * 0.45)
    # + (trajectory_score * 0.10)
    # + (volume_score * 0.10))

    un_gated_score = ((c_score * 0.35)
                      + (r_score * 0.45)
                      + (t_score * 0.10))

    return un_gated_score
