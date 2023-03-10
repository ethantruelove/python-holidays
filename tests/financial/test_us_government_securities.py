#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date
from datetime import timedelta as td

import holidays
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, SEP, OCT, NOV, DEC


class TestUnitedStatesGovernmentSecurities(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UnitedStatesGovernmentSecurities()

    def test_new_years(self):
        for dt in [
            date(1930, JAN, 1),
            date(1950, JAN, 2),
            date(1999, JAN, 1),
            date(2010, JAN, 1),
            date(2018, JAN, 1),
            date(2019, JAN, 1),
            date(2020, JAN, 1),
            date(2021, JAN, 1),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)

        for dt in [
            date(1999, DEC, 31),
            date(2000, JAN, 1),
            date(2021, DEC, 31),
            date(2022, JAN, 1),
            date(2027, DEC, 31),
            date(2028, JAN, 1),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_mlk(self):
        for dt in [
            date(1997, JAN, 20),
            date(1999, JAN, 18),
            date(2000, JAN, 17),
            date(2010, JAN, 18),
            date(2018, JAN, 15),
            date(2019, JAN, 21),
            date(2020, JAN, 20),
            date(2021, JAN, 18),
            date(2022, JAN, 17),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

        for dt in [
            date(1985, JAN, 21),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_washington(self):
        for dt in [
            date(1900, FEB, 22),
            date(1930, FEB, 21),
            date(1950, FEB, 22),
            date(1960, FEB, 22),
            date(1965, FEB, 22),
            date(1970, FEB, 23),
            date(1971, FEB, 15),
            date(1999, FEB, 15),
            date(2000, FEB, 21),
            date(2010, FEB, 15),
            date(2018, FEB, 19),
            date(2019, FEB, 18),
            date(2020, FEB, 17),
            date(2021, FEB, 15),
            date(2022, FEB, 21),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

    def test_good_friday(self):
        for dt in [
            date(2000, APR, 21),
            date(2018, MAR, 30),
            date(2019, APR, 19),
            date(2020, APR, 10),
            date(2022, APR, 15),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

        for dt in [
            date(1999, APR, 2),
            date(2010, APR, 2),
            date(2021, APR, 2),
            date(2023, APR, 7),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_memday(self):
        for dt in [
            date(1930, MAY, 30),
            date(1950, MAY, 30),
            date(1960, MAY, 30),
            date(1965, MAY, 31),
            date(1971, MAY, 31),
            date(1999, MAY, 31),
            date(2000, MAY, 29),
            date(2010, MAY, 31),
            date(2018, MAY, 28),
            date(2019, MAY, 27),
            date(2020, MAY, 25),
            date(2021, MAY, 31),
            date(2022, MAY, 30),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

    def test_juneteenth(self):
        for dt in [
            date(2021, JUN, 18),
            date(2022, JUN, 20),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

        for dt in [
            date(1954, JUN, 18),
            date(1967, JUN, 19),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_laborday(self):
        for dt in [
            date(1950, SEP, 4),
            date(1999, SEP, 6),
            date(2000, SEP, 4),
            date(2010, SEP, 6),
            date(2018, SEP, 3),
            date(2019, SEP, 2),
            date(2020, SEP, 7),
            date(2021, SEP, 6),
            date(2022, SEP, 5),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

    def test_columbusday(self):
        for dt in [
            date(1915, OCT, 12),
            date(1920, OCT, 12),
            date(1935, OCT, 11),
            date(1945, OCT, 12),
            date(1953, OCT, 12),
            date(1954, OCT, 12),
            date(2022, OCT, 12),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

    def test_veteransday(self):
        for dt in [
            date(1918, NOV, 11),
            date(1921, NOV, 11),
            date(1934, NOV, 12),
            date(1938, NOV, 11),
            date(1942, NOV, 11),
            date(1946, NOV, 11),
            date(1953, NOV, 11),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

        for dt in [
            date(1950, NOV, 11),
            date(2000, NOV, 11),
            date(2006, NOV, 11),
            date(2023, NOV, 11),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_thxgiving(self):
        for dt in [
            date(1901, NOV, 28),
            date(1902, NOV, 27),
            date(1950, NOV, 23),
            date(1999, NOV, 25),
            date(2000, NOV, 23),
            date(2010, NOV, 25),
            date(2018, NOV, 22),
            date(2019, NOV, 28),
            date(2020, NOV, 26),
            date(2021, NOV, 25),
            date(2022, NOV, 24),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=+7), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

    def test_christmas_day(self):
        for dt in [
            date(1901, DEC, 25),
            date(1902, DEC, 25),
            date(1950, DEC, 25),
            date(1999, DEC, 24),
            date(2000, DEC, 25),
            date(2010, DEC, 24),
            date(2018, DEC, 25),
            date(2019, DEC, 25),
            date(2020, DEC, 25),
            date(2021, DEC, 24),
            date(2022, DEC, 26),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=-7), self.holidays)

    def test_special_holidays(self):
        # add to this list as new historical holidays are added
        special_holidays = [
            date(2012, OCT, 30),  # Hurricane Sandy
            date(2018, DEC, 5),  # Death of George H.W. Bush
        ]

        for dt in special_holidays:
            self.assertIn(dt, self.holidays)

    def test_all_modern_holidays_present(self):
        usgs_2023 = holidays.UnitedStatesGovernmentSecurities(years=[2023])
        all_holidays = [
            "New Year's Day (Observed)",
            "Martin Luther King Jr. Day",
            "Washington's Birthday",
            "Memorial Day",
            "Juneteenth National Independence Day",
            "Independence Day",
            "Labor Day",
            "Thanksgiving Day",
            "Christmas Day",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, usgs_2023.values())

        self.assertNotIn("Good Friday", usgs_2023.values())
        self.assertNotIn("Veterans Day", usgs_2023.values())
