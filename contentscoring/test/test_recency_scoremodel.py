import mongomock
import nose.tools as nose_tools

from contentscoring.scoresubmodel import recency_score
from contentscoring.test import test_records_recency as t_rec

# Initialize pre-test mongomock
# sm_db = mongomock.MongoClient().db

# Divisor use as base divisor for time range divisor calculation.
# Base is nothing but the business days with in time range.
BASE_DIVISOR = 5


# 1 month score test cases
def test_trajectory_1month_high_score():
    score_out = recency_score(t_rec.recency_month_high_score_date_range,
                              t_rec.recency_month_high_score_date_visit_range, BASE_DIVISOR, 1)
    assert score_out == 100


def test_trajectory_1month_low_score():
    score_out = recency_score(t_rec.recency_month_low_score_date_range, t_rec.recency_month_low_score_date_visit_range,
                              BASE_DIVISOR, 1)
    assert score_out == 0


def test_trajectory_1month_random_score():
    score_out = recency_score(t_rec.recency_month_random_score_date_range,
                              t_rec.recency_month_random_score_date_visit_range, BASE_DIVISOR, 1)
    assert score_out == 90


# 3 months score test cases
def test_trajectory_3month_high_score():
    score_out = recency_score(t_rec.recency_3month_high_score_date_range,
                              t_rec.recency_3month_high_score_date_visit_range, BASE_DIVISOR, 3)
    assert score_out == 100


def test_trajectory_3month_low_score():
    score_out = recency_score(t_rec.recency_3month_low_score_date_range,
                              t_rec.recency_3month_low_score_date_visit_range, BASE_DIVISOR, 3)
    assert score_out == 0


def test_trajectory_3month_random_score():
    score_out = recency_score(t_rec.recency_3month_random_score_date_range,
                              t_rec.recency_3month_random_score_date_visit_range, BASE_DIVISOR, 3)
    assert score_out == 30


# 6 months score test cases
def test_trajectory_6month_high_score():
    score_out = recency_score(t_rec.recency_6month_high_score_date_range,
                              t_rec.recency_6month_high_score_date_visit_range, BASE_DIVISOR, 6)
    assert score_out == 100


def test_trajectory_6month_low_score():
    score_out = recency_score(t_rec.recency_6month_low_score_date_range,
                              t_rec.recency_6month_low_score_date_visit_range, BASE_DIVISOR, 6)
    assert score_out == 0


def test_trajectory_6month_random_score():
    score_out = recency_score(t_rec.recency_6month_random_date_range,
                              t_rec.recency_6month_random_date_visit_range, BASE_DIVISOR, 6)
    assert score_out == 70


# 1 years score test cases
def test_trajectory_year_high_score():
    score_out = recency_score(t_rec.recency_year_high_score_date_range,
                              t_rec.recency_year_high_score_date_visit_range, BASE_DIVISOR, 13)
    assert score_out == 100


def test_trajectory_year_low_score():
    score_out = recency_score(t_rec.recency_year_low_score_date_range,
                              t_rec.recency_year_low_score_date_visit_range, BASE_DIVISOR, 13)
    assert score_out == 0


def test_trajectory_year_random_score():
    score_out = recency_score(t_rec.recency_year_random_date_range,
                              t_rec.recency_year_random_date_visit_range, BASE_DIVISOR, 13)
    assert score_out == 60
