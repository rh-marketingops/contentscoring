# pylint: disable=C0103
"""
score model ungated test record sets.
"""

# import mongomock
# import nose.tools as nose_tools

from contentscoring.scoremodel import ungated_score
from contentscoring.test import test_records_ungatedscore as t_rec

# Initialize pre-test mongomock
# sm_db = mongomock.MongoClient().db


def test_ungated_1month_score():
    """

    :return:
    """

    ungated_score_out = ungated_score(t_rec.ungated_month_score_record_1)

    score_out = (ungated_score_out + (t_rec.ungated_month_score_record_1['vol_score'] * 0.10))

    assert score_out == 82


def test_ungated_3month_score():
    """

    :return:
    """

    ungated_score_out = ungated_score(t_rec.ungated_3month_score_record_1)

    score_out = (ungated_score_out + (t_rec.ungated_3month_score_record_1['vol_score'] * 0.10))

    assert score_out == 82


def test_ungated_6month_score():
    """

    :return:
    """

    ungated_score_out = ungated_score(t_rec.ungated_6month_score_record_1)

    score_out = (ungated_score_out + (t_rec.ungated_6month_score_record_1['vol_score'] * 0.10))

    assert score_out == 82


def test_ungated_year_score():
    """

    :return:
    """

    ungated_score_out = ungated_score(t_rec.ungated_year_score_record_1)

    score_out = (ungated_score_out + (t_rec.ungated_year_score_record_1['vol_score'] * 0.10))

    assert score_out == 82
