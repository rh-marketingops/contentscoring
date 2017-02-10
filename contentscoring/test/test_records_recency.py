# pylint: disable=C0103
"""
Sub model recency score test record sets.
"""

recency_month_high_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                            'visit_range': (5, 5, 5, 5),
                            'divisor': 5,
                            'time_range': 1}
recency_month_low_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                           'visit_range': (0, 0, 0, 0),
                           'divisor': 5,
                           'time_range': 1}
recency_month_random_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                              'visit_range': (4, 9, 5, 5),
                              'divisor': 5,
                              'time_range': 1}

recency_3month_high_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                             'visit_range': (15, 15, 15, 15),
                             'divisor': 5,
                             'time_range': 3}
recency_3month_low_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                            'visit_range': (0, 0, 0, 0),
                            'divisor': 5,
                            'time_range': 3}
recency_3month_random_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                               'visit_range': (15, 31, 14, 6),
                               'divisor': 5,
                               'time_range': 3}

recency_6month_high_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                             'visit_range': (30, 30, 30, 30),
                             'divisor': 5,
                             'time_range': 6}
recency_6month_low_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                            'visit_range': (0, 0, 0, 0),
                            'divisor': 5,
                            'time_range': 6}
recency_6month_random_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                               'visit_range': (17, 24, 245, 77),
                               'divisor': 5,
                               'time_range': 6}

recency_year_high_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                           'visit_range': (65, 65, 65, 65),
                           'divisor': 5,
                           'time_range': 13}
recency_year_low_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                          'visit_range': (0, 0, 0, 0),
                          'divisor': 5,
                          'time_range': 13}
recency_year_random_score = {'date_range': ('range_4', 'range_3', 'range_3', 'range_1'),
                             'visit_range': (70, 94, 295, 7),
                             'divisor': 5,
                             'time_range': 13}
