import mongomock
import nose.tools as nose_tools

from contentscoring.scoresubmodel import completion_score
from contentscoring.test import test_records_completion as t_rec

# Initialize pre-test mongomock
# sm_db = mongomock.MongoClient().db

# Divisor use as base divisor for time range divisor calculation.
# Base is nothing but the business days with in time range.
BASE_DIVISOR = 5


# 1 month score test cases
def test_trajectory_1month_high_score():
    score_out = completion_score(t_rec.completion_month_high_score_file_download,
                                 t_rec.completion_month_high_score_web_visit)
    assert score_out == 100


def test_trajectory_1month_low_score():
    score_out = completion_score(t_rec.completion_month_low_score_file_download,
                                 t_rec.completion_month_low_score_web_visit)
    assert score_out == 0


def test_trajectory_1month_random_score():
    score_out = completion_score(t_rec.completion_month_random_score_file_download,
                                 t_rec.completion_month_random_score_web_visit)
    assert score_out == 0


# 3 months score test cases
def test_trajectory_3month_high_score():
    score_out = completion_score(t_rec.completion_3month_high_score_file_download,
                                 t_rec.completion_3month_high_score_web_visit)
    assert score_out == 100


def test_trajectory_3month_low_score():
    score_out = completion_score(t_rec.completion_3month_low_score_file_download,
                                 t_rec.completion_3month_low_score_web_visit)
    assert score_out == 0


def test_trajectory_3month_random_score():
    score_out = completion_score(t_rec.completion_3month_random_score_file_download,
                                 t_rec.completion_3month_random_score_web_visit)
    assert score_out == 90


# 6 months score test cases
def test_trajectory_6month_high_score():
    score_out = completion_score(t_rec.completion_6month_high_score_file_download,
                                 t_rec.completion_6month_high_score_web_visit)
    assert score_out == 100


def test_trajectory_6month_low_score():
    score_out = completion_score(t_rec.completion_6month_low_score_file_download,
                                 t_rec.completion_6month_low_score_web_visit)
    assert score_out == 0


def test_trajectory_6month_random_score():
    score_out = completion_score(t_rec.completion_6month_random_score_file_download,
                                 t_rec.completion_6month_random_score_web_visit)
    assert score_out == 100


# 1 years score test cases
def test_trajectory_year_high_score():
    score_out = completion_score(t_rec.completion_year_high_score_file_download,
                                 t_rec.completion_year_high_score_web_visit)
    assert score_out == 100


def test_trajectory_year_low_score():
    score_out = completion_score(t_rec.completion_year_low_score_file_download,
                                 t_rec.completion_year_low_score_web_visit)
    assert score_out == 0


def test_trajectory_year_random_score():
    score_out = completion_score(t_rec.completion_year_random_score_file_download,
                                 t_rec.completion_year_random_score_web_visit)
    assert score_out == 95
