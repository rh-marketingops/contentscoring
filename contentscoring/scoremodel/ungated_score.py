

from contentscoring.scoresubmodel import completion_score
from contentscoring.scoresubmodel import recency_score
from contentscoring.scoresubmodel import trajectory_score
from contentscoring.scoresubmodel import volume_score


def get_completion_score():
    return 0


def get_recency_score():
    return 0


def get_trajectory_score():
    return 0


def get_volume_score():
    return 0


def ungated_score():
    """

    :return:
    """

    completion_score = get_completion_score()

    recency_score = get_recency_score()

    trajectory_score = get_trajectory_score()

    volume_score = get_volume_score()

    un_gated_score = ((completion_score * 0.35) + (recency_score * 0.45) + (trajectory_score * 0.10)
                      + (volume_score * 0.10))

    return un_gated_score