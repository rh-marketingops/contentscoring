import mongomock

import nose.tools as nose_tools

from contentscoring.scoresubmodel import completion_score
from contentscoring.scoresubmodel import trajectory_score
from contentscoring.scoresubmodel import recency_score
from contentscoring.scoresubmodel import volume_score

from contentscoring.test.test_records import trajectory_1year_xrange, trajectory_1year_yrange
from contentscoring.test.test_records import trajectory_6month_score_xrange, trajectory_6month_score_yrange
from contentscoring.test.test_records import trajectory_3month_score_xrange, trajectory_3month_score_yrange
from contentscoring.test.test_records import trajectory_1month_score_xrange, trajectory_1month_score_yrange


## Initialize pre-test mongomock
sm_db = mongomock.MongoClient().db


def test_trajectory_1year_score():
    score_out = trajectory_score(trajectory_1year_yrange, trajectory_1year_xrange)
    print score_out
    assert score_out == 100


def test_trajectory_6month_score():
    score_out = trajectory_score(trajectory_6month_score_yrange, trajectory_6month_score_xrange)
    assert score_out == 0
    
    
def test_trajectory_3month_score():
    score_out = trajectory_score(trajectory_3month_score_yrange, trajectory_3month_score_xrange)
    assert score_out == 0


def test_trajectory_1month_score():
    score_out = trajectory_score(trajectory_1month_score_yrange, trajectory_1month_score_xrange)
    assert score_out == 0
