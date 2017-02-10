# pylint: disable=C0103
"""
Unit test cases for recency sub score model.
"""

# import mongomock
# import nose.tools as nose_tools

from contentscoring.scoresubmodel import recency_score
from contentscoring.test import test_records_recency as t_rec

# Initialize pre-test mongomock
# sm_db = mongomock.MongoClient().db

# Divisor use as base divisor for time range divisor calculation.
# Base is nothing but the business days with in time range.
BASE_DIVISOR = 5


# 1 month score test cases
def test_recency_1month_high_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_month_high_score['date_range'],
                              t_rec.recency_month_high_score['visit_range'],
                              t_rec.recency_month_high_score['divisor'],
                              t_rec.recency_month_high_score['time_range'])
    assert score_out == 100


def test_recency_1month_low_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_month_low_score['date_range'],
                              t_rec.recency_month_low_score['visit_range'],
                              t_rec.recency_month_low_score['divisor'],
                              t_rec.recency_month_low_score['time_range'])
    assert score_out == 0


def test_recency_1month_random_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_month_random_score['date_range'],
                              t_rec.recency_month_random_score['visit_range'],
                              t_rec.recency_month_random_score['divisor'],
                              t_rec.recency_month_random_score['time_range'])
    assert score_out == 90


# 3 months score test cases
def test_recency_3month_high_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_3month_high_score['date_range'],
                              t_rec.recency_3month_high_score['visit_range'],
                              t_rec.recency_3month_high_score['divisor'],
                              t_rec.recency_3month_high_score['time_range'])
    assert score_out == 100


def test_recency_3month_low_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_3month_low_score['date_range'],
                              t_rec.recency_3month_low_score['visit_range'],
                              t_rec.recency_3month_low_score['divisor'],
                              t_rec.recency_3month_low_score['time_range'])
    assert score_out == 0


def test_recency_3month_random_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_3month_random_score['date_range'],
                              t_rec.recency_3month_random_score['visit_range'],
                              t_rec.recency_3month_random_score['divisor'],
                              t_rec.recency_3month_random_score['time_range'])
    assert score_out == 30


# 6 months score test cases
def test_recency_6month_high_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_6month_high_score['date_range'],
                              t_rec.recency_6month_high_score['visit_range'],
                              t_rec.recency_6month_high_score['divisor'],
                              t_rec.recency_6month_high_score['time_range'])
    assert score_out == 100


def test_recency_6month_low_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_6month_low_score['date_range'],
                              t_rec.recency_6month_low_score['visit_range'],
                              t_rec.recency_6month_low_score['divisor'],
                              t_rec.recency_6month_low_score['time_range'])
    assert score_out == 0


def test_recency_6month_random_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_6month_random_score['date_range'],
                              t_rec.recency_6month_random_score['visit_range'],
                              t_rec.recency_6month_random_score['divisor'],
                              t_rec.recency_6month_random_score['time_range'])
    assert score_out == 70


# 1 years score test cases
def test_recency_year_high_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_year_high_score['date_range'],
                              t_rec.recency_year_high_score['visit_range'],
                              t_rec.recency_year_high_score['divisor'],
                              t_rec.recency_year_high_score['time_range'])
    assert score_out == 100


def test_recency_year_low_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_year_low_score['date_range'],
                              t_rec.recency_year_low_score['visit_range'],
                              t_rec.recency_year_low_score['divisor'],
                              t_rec.recency_year_low_score['time_range'])
    assert score_out == 0


def test_recency_year_random_score():
    """

    :return:
    """

    score_out = recency_score(t_rec.recency_year_random_score['date_range'],
                              t_rec.recency_year_random_score['visit_range'],
                              t_rec.recency_year_random_score['divisor'],
                              t_rec.recency_year_random_score['time_range'])
    assert score_out == 60
