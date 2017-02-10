"""
Unit test cases for trajectory sub score model.
"""

# import mongomock
# import nose.tools as nose_tools

from contentscoring.scoresubmodel import trajectory_score
from contentscoring.test import test_records_trajectory as t_rec

# Initialize pre-test mongomock
# sm_db = mongomock.MongoClient().db


def test_trajectory_1year_score():
    """

    :return:
    """

    score_out = trajectory_score(t_rec.trajectory_1year_yrange,
                                 t_rec.trajectory_1year_xrange)
    assert score_out == 100


def test_trajectory_6month_score():
    """

    :return:
    """

    score_out = trajectory_score(t_rec.trajectory_1month_score_xrange,
                                 t_rec.trajectory_6month_score_xrange)
    assert score_out == 0


def test_trajectory_3month_score():
    """

    :return:
    """

    score_out = trajectory_score(t_rec.trajectory_3month_score_yrange,
                                 t_rec.trajectory_3month_score_xrange)
    assert score_out == 0


def test_trajectory_1month_score():
    """

    :return:
    """

    score_out = trajectory_score(t_rec.trajectory_1month_score_yrange,
                                 t_rec.trajectory_1month_score_xrange)
    assert score_out == 0
