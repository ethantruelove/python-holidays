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

from datetime import date
from datetime import timedelta as td

from dateutil.easter import easter
from dateutil.relativedelta import MO, TH, FR
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, MAY, JUN, JUL, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class UnitedStatesGovernmentSecurities(HolidayBase):
    # Official regulations:
    # https://www.sifma.org/resources/general/holiday-schedule/#US
    # Historical data:
    # https://www.sifma.org/resources/general/us-holiday-archive/

    market = "USGS"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _get_observed(self, d):
        wdnum = d.isoweekday()
        if wdnum == 6:
            return d + rd(weekday=FR(-1))
        if wdnum == 7:
            return d + rd(weekday=MO(+1))
        return d

    def _set_observed_date(self, holiday_date, name):
        date_obs = self._get_observed(holiday_date)
        if date_obs == holiday_date:
            self[holiday_date] = name
        else:
            self[date_obs] = name + " (Observed)"

    def _populate(self, year):
        super()._populate(year)

        ##############################################################
        # REGULAR HOLIDAYS
        ##############################################################

        # NEW YEAR'S DAY
        # Similar to NYSE, if holiday is on a Saturday, there is no closure.
        nyd = date(year, JAN, 1)
        if not self._is_saturday(nyd):
            self._set_observed_date(nyd, "New Year's Day")

        # MLK DAY
        if year >= 1986:
            self[
                date(year, JAN, 1) + rd(weekday=MO(3))
            ] = "Martin Luther King Jr. Day"

        # WASHINGTON'S BIRTHDAY: Feb 22 (obs) until 1971, then 3rd Mon of Feb
        if year < 1971:
            wash = date(year, FEB, 22)
            self._set_observed_date(wash, "Washington's Birthday")
        else:
            self[
                date(year, FEB, 1) + rd(weekday=MO(3))
            ] = "Washington's Birthday"

        # GOOD FRIDAY - except when Employment Situation is released
        # https://www.bls.gov/ces/publications/news-release-schedule.htm
        # "The Employment Situation report is typically released
        # on the third Friday after the conclusion of the reference week,
        # i.e., the week which includes the 12th of the month."
        # This applies only to Good Friday as no other holiday will
        # exist on a Friday or be that early in the month.
        # add three weeks from reference date then get next Friday
        third_friday_after_reference = (
            date(year, MAR, 12) + td(days=21) + rd(weekday=FR(1))
        )
        good_friday = easter(year) + td(days=-2)
        if good_friday != third_friday_after_reference:
            self[good_friday] = "Good Friday"

        # MEM DAY (May 30)
        # last Mon in May since 1971
        if year < 1971:
            memday = date(year, MAY, 30)
            self._set_observed_date(memday, "Memorial Day")
        else:
            self[date(year, MAY, 31) + rd(weekday=MO(-1))] = "Memorial Day"

        # JUNETEENTH
        if year >= 2021:
            juneteenth = date(year, JUN, 19)
            self._set_observed_date(
                juneteenth, "Juneteenth National Independence Day"
            )

        # INDEPENDENCE DAY
        j4th = date(year, JUL, 4)
        self._set_observed_date(j4th, "Independence Day")

        # LABOR DAY
        self[date(year, SEP, 1) + rd(weekday=MO(1))] = "Labor Day"

        # COLOMBUS DAY
        colday = date(year, OCT, 12)
        self._set_observed_date(colday, "Columbus Day")

        # VETERANS DAY
        # Veterans Day is not observed when it falls on a Saturday
        # See historical examples (2023, 2006, 2000, etc.)
        vetday = date(year, NOV, 11)
        if not self._is_saturday(vetday):
            self._set_observed_date(vetday, "Veteran's Day")

        # THANKSGIVING DAY
        self[date(year, NOV, 1) + rd(weekday=TH(4))] = "Thanksgiving Day"

        # CHRISTMAS DAY
        xmas = date(year, DEC, 25)
        self._set_observed_date(xmas, "Christmas Day")

        ##############################################################
        # SPECIAL HOLIDAYS
        ##############################################################

        if year == 2012:
            self[date(year, OCT, 30)] = "Hurricane Sandy"

        if year == 2018:
            self[date(year, DEC, 5)] = "Death of George H.W. Bush"


class USGS(UnitedStatesGovernmentSecurities):
    pass
