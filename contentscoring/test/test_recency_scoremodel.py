import mongomock
import nose.tools as nose_tools

from contentscoring.scoresubmodel import recency_score

from contentscoring.test.test_records_recency import recency_month_date_range, recency_month_date_visit_range
from contentscoring.test.test_records_recency import recency_3month_date_range, recency_3month_date_visit_range
from contentscoring.test.test_records_recency import recency_6month_date_range, recency_6month_date_visit_range
from contentscoring.test.test_records_recency import recency_year_date_range, recency_year_visit_range


# Initialize pre-test mongomock
# sm_db = mongomock.MongoClient().db

BASE_DIVISOR = 5


def test_trajectory_1month_score():
    score_out = recency_score(recency_month_date_range, recency_month_date_visit_range, BASE_DIVISOR, 1)
    assert score_out == 90


def test_trajectory_3month_score():
    score_out = recency_score(recency_3month_date_range, recency_3month_date_visit_range, BASE_DIVISOR, 3)
    assert score_out == 30


def test_trajectory_6month_score():
    score_out = recency_score(recency_6month_date_range, recency_6month_date_visit_range, BASE_DIVISOR, 6)
    assert score_out == 100


def test_trajectory_year_score():
    score_out = recency_score(recency_year_date_range, recency_year_visit_range, BASE_DIVISOR, 13)
    assert score_out == 40
