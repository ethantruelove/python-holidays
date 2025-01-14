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

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import _ThaiLuniSolar


class Thailand(HolidayBase):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Thailand. (Based on South Korean and Singaporean Implementation)


    References:

    - Based on: https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    - Checked with: (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_2023
    - [In Lieus]
        (isranews.org 's wbm) http://tiny.cc/wa_isranews_inlieu_hist
        https://resolution.soc.go.th/?prep_id=99159317
        https://resolution.soc.go.th/?prep_id=196007
        https://github.com/dr-prodigy/python-holidays/pull/929
    - [New Year's Day]
        (wikisource.org 's wbm) http://tiny.cc/wa_wiki_thai_newyear_2483
    - [Chakri Memorial Day]
        (ocac.got.th 's wbm) http://tiny.cc/wa_ocac_chakri
    - [Songkran Festival]
        (museumsiam.org 's wbm) http://tiny.cc/wa_museumsiam_songkran
        https://resolution.soc.go.th/?prep_id=123659
    - [National Labour Day]
        https://www.thairath.co.th/lifestyle/culture/1832869
    - [National Day (24 June: Defunct)]
        (Ministry of Culture 's wbm) http://tiny.cc/wa_mincul_nat_day
    - [Coronation Day]
        https://www.matichon.co.th/politics/news_526200
        https://workpointtoday.com/news1-5/
    - [HM Queen Suthida's Birthday]
        https://www.thairath.co.th/news/politic/1567418
    - [HM Maha Vajiralongkorn's Birthday]
        https://www.matichon.co.th/politics/news_526200
    - [HM Queen Sirikit the Queen Mother's Birthday]
        https://hilight.kapook.com/view/14164
    - [National Mother's Day]
        https://www.brh.go.th/index.php/2019-02-27-04-11-52/542-12-2564
    - [HM King Bhumibol Adulyadej Memorial Day]
        https://www.matichon.co.th/politics/news_526200
    - [Chulalongkorn Memorial Day]
        https://th.wikipedia.org/wiki/วันปิยมหาราช
    - [HM King Bhumibol Adulyadej's Birthday]
        (Ministry of Culture 's wbm) http://tiny.cc/wa_mincul_nat_day
        https://hilight.kapook.com/view/148862
    - [National Father's Day]
        https://www.brh.go.th/index.php/2019-02-27-04-12-21/594-5-5
    - [Constitution Day]
        https://hilight.kapook.com/view/18208
        (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992
        https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2475.aspx
    - [New Year's Eve]
        (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992
        https://resolution.soc.go.th/?prep_id=205799
        https://resolution.soc.go.th/?prep_id=210744
    - [Makha Bucha]
        https://www.onab.go.th/th/content/category/detail/id/73/iid/3403
    - [Visakha Bucha]
        https://www.onab.go.th/th/content/category/detail/id/73/iid/3401
    - [Asarnha Bucha]
        https://www.onab.go.th/th/content/category/detail/id/73/iid/3397
    - [Buddhist Lent Day]
        https://www.onab.go.th/th/content/category/detail/id/73/iid/3395
    - [Royal Ploughing Ceremony]
        https://en.wikipedia.org/wiki/Royal_Ploughing_Ceremony
        https://www.lib.ru.ac.th/journal/may/may_phauchmongkol.html
        https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2540.aspx


    Limitations:

    - This is only 100% accurate for 1997-2023; any future dates are up to the
      Royal Thai Government Gazette which updates on a year-by-year basis.

    - Approx. date only goes as far back as 1941 (B.E. 2484) as the Thai
      calendar for B.E. 2483 as we only have nine months from switching
      New Year Date (April 1st to January 1st).

    - Thai Lunar Calendar Holidays only work from 1941 (B.E. 2484) onwards
      until 2057 (B.E. 2600) as we only have Thai year-type data for
      cross-checking until then.

    - Royal Ploughing Ceremony Day is date is announced on an annual basis
      by the Court Astrologers, thus need an annual update to the library here

    - This doesn't cover Thai regional public holidays yet, only stubs added


    Country created by: `arkid15r <https://github.com/arkid15r>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """

    country = "TH"

    # วันหยุดพิเศษ (เพิ่มเติม) - see Bank of Thailand's DB for Cross-Check
    thai_special_in_lieu_holidays = "Special In Lieu Holiday"
    thai_election = "Thai Election Day"
    thai_election_in_lieu = "Thai Election Day (in lieu)"
    thai_bridge_public_holiday = "Bridge Public Holiday"

    # Special Cases
    rama_ix_golden_jubilee = "HM King Bhumibol Adulyadej's Golden Jubilee"
    rama_ix_sixty_accession = (
        "HM King Bhumibol Adulyadej's 60th Anniversary of Accession Event"
    )
    thai_military_emergency_lockdown = (
        "Emergency Lockdown (Thai Military Coup d'état)"
    )
    thai_political_emergency_lockdown = (
        "Emergency Lockdown (Thai Political Unrest)"
    )
    thai_flood_2011_emergency_lockdown = (
        "Emergency Lockdown (2011 Thailand Floods)"
    )
    rama_ix_mourning = "Day of Mourning for HM King Bhumibol Adulyadej"
    rama_ix_cremation = "HM King Bhumibol Adulyadej's Royal Cremation Ceremony"
    rama_x_coronation_celebrations = (
        "HM King Maha Vajiralongkorn's Coronation Celebrations"
    )
    songkran_festival_in_lieu_covid = "Songkran Festival (in lieu)"

    special_holidays = {
        # 1992-1994 (include In Lieus, Checked with Bank of Thailand Data)
        1992: (
            (MAY, 18, thai_special_in_lieu_holidays),
            (DEC, 7, thai_special_in_lieu_holidays),
        ),
        1993: (
            (MAR, 8, thai_special_in_lieu_holidays),
            (MAY, 3, thai_special_in_lieu_holidays),
            (OCT, 25, thai_special_in_lieu_holidays),
            (DEC, 6, thai_special_in_lieu_holidays),
        ),
        1994: (
            (JAN, 3, thai_special_in_lieu_holidays),
            (MAY, 2, thai_special_in_lieu_holidays),
            (JUL, 25, thai_special_in_lieu_holidays),
            (OCT, 24, thai_special_in_lieu_holidays),
            (DEC, 12, thai_special_in_lieu_holidays),
        ),
        # 1995-1997 (Bank of Thailand Data)
        1996: ((JUN, 10, rama_ix_golden_jubilee),),
        # 1998-2000 (include In Lieus, Checked with Bank of Thailand Data)
        1998: (
            (MAY, 11, thai_special_in_lieu_holidays),
            (DEC, 7, thai_special_in_lieu_holidays),
        ),
        1999: (
            (MAY, 3, thai_special_in_lieu_holidays),
            (MAY, 31, thai_special_in_lieu_holidays),
            (OCT, 25, thai_special_in_lieu_holidays),
            (DEC, 6, thai_special_in_lieu_holidays),
        ),
        2000: (
            (JAN, 3, thai_special_in_lieu_holidays),
            (FEB, 21, thai_special_in_lieu_holidays),
            (AUG, 14, thai_special_in_lieu_holidays),
            (DEC, 11, thai_special_in_lieu_holidays),
            (DEC, 29, thai_election),
        ),
        # From 2001 Onwards (Checked with Bank of Thailand Data)
        2006: (
            (APR, 19, thai_election),
            (JUN, 9, rama_ix_sixty_accession),
            (JUN, 12, rama_ix_sixty_accession),
            (JUN, 13, rama_ix_sixty_accession),
            (SEP, 20, thai_military_emergency_lockdown),
        ),
        2007: ((DEC, 24, thai_election_in_lieu),),
        2009: (
            (JAN, 2, thai_bridge_public_holiday),
            (APR, 10, thai_political_emergency_lockdown),
            (APR, 16, thai_political_emergency_lockdown),
            (APR, 17, thai_political_emergency_lockdown),
            (JUL, 6, thai_bridge_public_holiday),
        ),
        2010: (
            (MAY, 20, thai_bridge_public_holiday),
            (MAY, 21, thai_bridge_public_holiday),
            (AUG, 13, thai_bridge_public_holiday),
        ),
        2011: (
            (MAY, 16, thai_bridge_public_holiday),
            (OCT, 27, thai_flood_2011_emergency_lockdown),
            (OCT, 28, thai_flood_2011_emergency_lockdown),
            (OCT, 31, thai_flood_2011_emergency_lockdown),
        ),
        2012: ((APR, 9, thai_bridge_public_holiday),),
        2013: ((DEC, 30, thai_bridge_public_holiday),),
        2014: ((AUG, 11, thai_bridge_public_holiday),),
        2015: (
            (JAN, 2, thai_bridge_public_holiday),
            (MAY, 4, thai_bridge_public_holiday),
        ),
        2016: (
            (MAY, 6, thai_bridge_public_holiday),
            (JUL, 18, thai_bridge_public_holiday),
            (OCT, 14, rama_ix_mourning),
        ),
        2017: ((OCT, 26, rama_ix_cremation),),
        2019: ((MAY, 6, rama_x_coronation_celebrations),),
        2020: (
            (JUL, 27, songkran_festival_in_lieu_covid),
            (SEP, 4, songkran_festival_in_lieu_covid),
            (SEP, 7, songkran_festival_in_lieu_covid),
            (NOV, 19, thai_bridge_public_holiday),
            (NOV, 20, thai_bridge_public_holiday),
            (DEC, 11, thai_bridge_public_holiday),
        ),
        2021: (
            (FEB, 12, thai_bridge_public_holiday),
            (APR, 12, thai_bridge_public_holiday),
            (SEP, 24, thai_bridge_public_holiday),
        ),
        2022: (
            (JUL, 15, thai_bridge_public_holiday),
            (JUL, 29, thai_bridge_public_holiday),
            (OCT, 14, thai_bridge_public_holiday),
            (DEC, 30, thai_bridge_public_holiday),
        ),
        2023: ((MAY, 5, thai_bridge_public_holiday),),
    }

    def __init__(self, **kwargs) -> None:
        self.thls = _ThaiLuniSolar()
        super().__init__(**kwargs)

    def _populate(self, year):
        # Due to Thai Calendar Migration, this is capped off at 1941
        # But certain holidays were implemented before 1941
        if year <= 1940:
            return None

        def _add_with_observed(dt, holiday_name) -> None:
            # TODO: add `if dt.year == year` check for Islamic holidays
            # which can straddle across gregorian years in southern region.
            self[dt] = holiday_name

            """
            !!! If Public Holiday falls on weekends, (in lieu) on workday !!!
            Despite the wording, this usually only applies to Monday only for
            holidays, consecutive holidays all have their own special in lieu
            declared separately.

            Data from 1992-1994 and 1998-2000 are declared discretely in
            special_holidays declarations above.

            Applied Automatically for Monday if on Weekends: 1961-1973
             **NOTE: No New Year's Eve (in lieu) for this period
            No In Lieu days available: 1974-1988
            Case-by-Case application for Workday if on Weekends: 1989-1994
            Applied Automatically for Workday if on Weekends: 1995-1997
            Case-by-Case application for Workday if on Weekends: 1998-2000
            Applied Automatically for Workday if on Weekends: 2001-Present
            """
            if 1961 <= year <= 1973 or 1995 <= year <= 1997 or year >= 2001:
                if self.observed and self._is_weekend(dt):
                    in_lieu = dt + td(days=+2 if self._is_saturday(dt) else +1)
                    self[in_lieu] = f"{holiday_name} (in lieu)"

        super()._populate(year)

        ########################
        #
        # FIXED DATED HOLIDAYS
        #
        ########################

        # !!! New Year's Day !!!
        # วันขึ้นปีใหม่
        # Status: In-Use
        # Starts in the present form in 1941 (B.E. 2484)
        # TODO: Add check for 1941 if we support earlier dates.

        _add_with_observed(date(year, JAN, 1), "New Year's Day")

        # !!! New Year's Eve (in lieu) !!!
        # วันหยุดชดเชยวันสิ้นปี
        # Status: In-Use
        # Added separately from New Year's Eve itself so that it would't
        #   go over the next year
        #   - CASE 1: SAT-SUN -> 1 in-lieu on TUE
        #   - CASE 2: SUN-MON -> 1 in-lieu on TUE
        # See in lieu logic in `_add_with_observed(dt, holiday_name)`
        new_years_eve_in_lieu = "New Year's Eve (in lieu)"

        if self.observed and (1995 <= year <= 1997 or year >= 2001):
            if self._is_saturday(date(year - 1, DEC, 31)):
                self[date(year, JAN, 3)] = new_years_eve_in_lieu
            elif self._is_sunday(date(year - 1, DEC, 31)):
                self[date(year, JAN, 2)] = new_years_eve_in_lieu

        # !!! Chakri Memorial Day !!!
        # วันจักรี
        # Status: In-Use
        # Starts in present form in 1918 (B.E. 2461)
        # TODO: Add check for 1918 if we support earlier dates.

        _add_with_observed(date(year, APR, 6), "Chakri Memorial Day")

        # !!! Songkran Festival !!!
        # วันสงกรานต์
        # Status: In-Use
        # Used to be April 1st as Thai New Year Day
        # Initially abandoned in 1941 (B.E. 2484), declared again as
        #   public holidays in 1948 (2491 B.E)
        #  - 1948-1953, celebrated on Apr 13-15
        #  - 1954-1956, abandoned as a public holiday
        #  - 1957-1988, only celebrated on Apr 13
        #  - 1989-1997, celebrated on Apr 12-14
        #  - 1998-Present, celebrated on Apr 13-15
        #    (Except for 2020 due to Covid-19 outbreaks)
        # This has its own in-lieu trigger
        songkran_festival = "Songkran Festival"

        if 1948 <= year <= 1953:
            self[date(year, APR, 13)] = songkran_festival
            self[date(year, APR, 14)] = songkran_festival
            self[date(year, APR, 15)] = songkran_festival
        elif 1957 <= year <= 1988:
            _add_with_observed(date(year, APR, 13), songkran_festival)
        elif 1989 <= year <= 1997:
            self[date(year, APR, 12)] = songkran_festival
            self[date(year, APR, 13)] = songkran_festival
            self[date(year, APR, 14)] = songkran_festival
        elif year >= 1998 and year != 2020:
            self[date(year, APR, 13)] = songkran_festival
            self[date(year, APR, 14)] = songkran_festival
            self[date(year, APR, 15)] = songkran_festival

        # !!! Songkran Festival (in lieu) !!!
        # วันหยุดชดเชยวันสงกรานต์
        # If Songkran happened to be held on the weekends, only one in-lieu
        #   public holiday is added, No in lieus for SUN-MON-TUE case
        #   - CASE 1: THU-FRI-SAT -> 1 in-lieu on MON
        #   - CASE 2: FRI-SAT-SUN -> 1 in-lieu on MON
        #   - CASE 3: SAT-SUN-MON -> 1 in-lieu on TUE
        # See in lieu logic in `_add_with_observed(dt, holiday_name)`
        # Status: In Use

        songkran_festival_in_lieu = "Songkran Festival (in lieu)"

        if self.observed and (1995 <= year <= 1997 or year >= 2001):
            dt = date(year, APR, 15) if year >= 2001 else date(year, APR, 14)

            if self._is_saturday(dt):
                self[dt + td(days=+2)] = songkran_festival_in_lieu
            elif self._is_sunday(dt):
                self[dt + td(days=+1)] = songkran_festival_in_lieu
            elif self._is_monday(dt):
                self[dt + td(days=+1)] = songkran_festival_in_lieu

        # !!! National Labour day !!!
        # วันแรงงานแห่งชาติ
        # Status: In-Use
        # Starts in the present form in 1974 (B.E. 2517)
        # Does existed officially since 1956 (B.E. 2499),
        #   but wasn't a public holiday until then
        # *** NOTE: only observed by financial and private sectors

        if year >= 1974:
            _add_with_observed(date(year, MAY, 1), "National Labour Day")

        # !!! National Day (24 June) !!!
        # วันชาติ
        # Status: Defunct (Historical)
        # Starts in 1939 (B.E. 2482) by Plaek Phibunsongkhram
        # Replaced by Rama IX's birthday in 1960 (B.E. 2503) by Sarit Thanarat
        # TODO: Add check for 1939 if we support earlier dates.

        if year <= 1959:
            _add_with_observed(date(year, JUN, 24), "National Day")

        # !!! Coronation Day !!!
        # วันฉัตรมงคล
        # Starts in 1958 (B.E. 2501) for Rama IX's Coronation: May 5th
        # No celebration in 2017-2019 (B.E 2560-2562)
        # Reestablished with Rama X's Coronation in 2020: May 4th
        coronation_day = "Coronation Day"

        if 1958 <= year <= 2016:
            _add_with_observed(date(year, MAY, 5), coronation_day)
        elif year >= 2020:
            _add_with_observed(date(year, MAY, 4), coronation_day)

        # !!! HM Queen Suthida's Birthday !!!
        # วันเฉลิมพระชนมพรรษา พระราชินี
        # Status: In-Use
        # Starts in 2019 (B.E. 2562)

        if year >= 2019:
            _add_with_observed(
                date(year, JUN, 3), "HM Queen Suthida's Birthday"
            )

        # !!! HM King Maha Vajiralongkorn's Birthday !!!
        # วันเฉลิมพระชนมพรรษา รัชกาลที่ 10
        # Status: In-Use
        # Started in 2017 (B.E 2560)

        if year >= 2017:
            _add_with_observed(
                date(year, JUL, 28), "HM King Maha Vajiralongkorn's Birthday"
            )

        # !!! HM Queen Sirikit the Queen Mother's Birthday !!!
        # วันเฉลิมพระชนมพรรษา พระบรมราชินีนาถ ( 1976-2017),
        # วันเฉลิมพระชนมพรรษา พระบรมราชชนนีพันปีหลวง (2017-Present)
        # Status: In-Use
        # Started in 1976 (B.E. 2519) alongside Mother's Day
        # Initial celebration as HM Queen Sirikit's Birthday
        # Now acts as the Queen Mother from 2017 onwards.

        if 1976 <= year <= 2016:
            _add_with_observed(
                date(year, AUG, 12), "HM Queen Sirikit's Birthday"
            )
        elif year >= 2017:
            _add_with_observed(
                date(year, AUG, 12),
                "HM Queen Sirikit The Queen Mother's Birthday",
            )

        # !!! National Mother's Day !!!
        # วันแม่แห่งชาติ
        # Status: In-Use
        # Started 1950 (B.E 2493) initially as April 15 and cancelled in
        #   1958 (B.E 2501) when the Min. of Culture was abolished.
        # Restarts again in 1976 (B.E. 2519) on Queen Sirikit's Birthday
        #   (August 12) and stay that way from that point onwards.
        thai_mothers_day = "National Mother's Day"

        if 1950 <= year <= 1957:
            _add_with_observed(date(year, APR, 15), thai_mothers_day)
        elif year >= 1976:
            _add_with_observed(date(year, AUG, 12), thai_mothers_day)

        # !!! Anniversary for the Death of King Bhumibol Adulyadej !!!
        # วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทร มหาภูมิพลอดุลยเดช บรมนาถบพิตร
        # Status: In-Use
        # Started in 2017 (B.E 2560)

        if year >= 2017:
            _add_with_observed(
                date(year, OCT, 13), "HM King Bhumibol Adulyadej Memorial Day"
            )

        # !!! Chulalongkorn Memorial Day !!!
        # วันปิยมหาราช
        # Status: In-Use
        # Started in 1911 (B.E. 2454)
        # TODO: Add check for 1911 if we support earlier dates.

        _add_with_observed(date(year, OCT, 23), "Chulalongkorn Memorial Day")

        # !!! HM King Bhumibol Adulyadej's Birthday Anniversary !!!
        # วันเฉลิมพระชนมพรรษา รัชกาลที่ 9 (1960-2016),
        # วันคล้ายยวันเฉลิมพระชนมพรรษา รัชกาลที่ 9 (2017-Present)
        # Status: In-Use
        # Replaced Nataion Day (26 June) in 1960 (B.E. 2503) by Sarit Thanarat
        # Confirmed as still in-use in 2017

        if year >= 1960:
            _add_with_observed(
                date(year, DEC, 5), "HM King Bhumibol Adulyadej's Birthday"
            )

        # !!! National Father's Day !!!
        # วันพ่อแห่งชาติ
        # Status: In-Use
        # Starts in 1980 (B.E 2523)
        # Technically, a replication of HM King Bhumibol Adulyadej's Birthday
        #   but it's in the official calendar, so may as well have this here

        if year >= 1980:
            _add_with_observed(date(year, DEC, 5), "National Father's Day")

        # !!! Constitution Day !!!
        # วันรัฐธรรมนูญ
        # Status: In-Use
        # Presumed to starts in 1932 (B.E. 2475) ???
        # Last known official record is Bank of Thailand's in 1992 (B.E. 2535)
        # TODO: Add check for 1932 if we support earlier dates.

        _add_with_observed(date(year, DEC, 10), "Constitution Day")

        # !!! New Year's Eve !!!
        # วันสิ้นปี
        # Status: In-Use
        # Presumed to start in the present form in 1941 (B.E. 2484) ???
        # Last known official record is Bank of Thailand's in 1992 (B.E. 2535)
        # TODO: Add check for 1941 if we support earlier dates.
        # This has its own in-lieu trigger

        self[date(year, DEC, 31)] = "New Year's Eve"

        ################################
        #
        # THAI LUNAR CALENDAR HOLIDAYS
        #
        ################################

        """
        See `_ThaiLuniSolar` in holidays/utils.py for more details.

        Thai Lunar Calendar Holidays only work from 1941 (B.E. 2484) onwards
        until 2057 (B.E. 2600).
        """
        # !!! Makha Bucha !!!
        # วันมาฆบูชา
        # Status: In-Use

        makha_bucha_date = self.thls.makha_bucha_date(year)
        if makha_bucha_date:
            _add_with_observed(makha_bucha_date, "Makha Bucha")

        # !!! Visakha Bucha !!!
        # วันวิสาขบูชา
        # Status: In-Use

        visakha_bucha_date = self.thls.visakha_bucha_date(year)
        if visakha_bucha_date:
            _add_with_observed(visakha_bucha_date, "Visakha Bucha")

        # !!! Asarnha Bucha !!!
        # วันอาสาฬหบูชา
        # Status: In-Use
        # This has its own in-lieu trigger

        asarnha_bucha_date = self.thls.asarnha_bucha_date(year)
        if asarnha_bucha_date:
            self[asarnha_bucha_date] = "Asarnha Bucha"

        # !!! Buddhist Lent Day !!!
        # วันเข้าพรรษา
        # Status: In-Use
        # This has its own in-lieu trigger

        khao_phansa_date = self.thls.khao_phansa_date(year)
        if khao_phansa_date:
            self[khao_phansa_date] = "Buddhist Lent Day"

        # !!! Asarnha Bucha/Buddhist Lent Day (in lieu) !!!
        # วันหยุดชดเชยวันอาสาฬหบูชา
        # วันหยุดชดเชยวันเข้าพรรษา
        # Status: In Use
        #  - CASE 1: FRI-SAT -> 1 in-lieu on MON
        #  - CASE 2: SAT-SUN -> 1 in-lieu on MON
        #  - CASE 3: SUN-MON -> 1 in-lieu on TUE
        # See in lieu logic in `_add_with_observed(dt, holiday_name)`

        if (
            asarnha_bucha_date
            and self.observed
            and (1961 <= year <= 1973 or 1995 <= year <= 1997 or year >= 2001)
        ):
            if self._is_friday(asarnha_bucha_date):
                self[
                    asarnha_bucha_date + td(days=+3)
                ] = "Buddhist Lent Day (in lieu)"
            elif self._is_weekend(asarnha_bucha_date):
                self[
                    asarnha_bucha_date + td(days=+2)
                ] = "Asarnha Bucha (in lieu)"

        #################################
        #
        # NO FUTURE FIXED DATE HOLIDAYS
        #
        #################################

        # !!! Royal Ploughing Ceremony !!!
        # วันพืชมงคล
        # Restarts in 1957 (B.E. 2500)
        # Is dated on an annual basis by the Royal Palace
        # This isn't even fixed even by the Thai Lunar Calendar, but instead
        #   by Court Astrologers; All chosen dates are all around May, so we
        #   can technically assign it to 13 May for years prior with no data.
        # *** NOTE: only observed by government sectors
        # TODO: Update this annually around Dec of each year
        raeknakhwan = "Royal Ploughing Ceremony"

        raeknakhwan_dates = {
            1997: (MAY, 13),
            1998: (MAY, 13),
            # Not held in 1999 date
            2000: (MAY, 15),
            2001: (MAY, 16),
            2002: (MAY, 9),
            2003: (MAY, 8),
            2004: (MAY, 7),
            2005: (MAY, 11),
            2006: (MAY, 11),
            2007: (MAY, 10),
            2008: (MAY, 9),
            2009: (MAY, 11),
            2010: (MAY, 10),
            2011: (MAY, 13),
            2012: (MAY, 9),
            2013: (MAY, 13),
            2014: (MAY, 9),
            2015: (MAY, 13),
            2016: (MAY, 9),
            2017: (MAY, 12),
            2018: (MAY, 14),
            2019: (MAY, 9),
            2020: (MAY, 11),
            2021: (MAY, 13),
            2022: (MAY, 17),
            2023: (MAY, 11),
        }
        # For years with exact date data
        if year in raeknakhwan_dates:
            _add_with_observed(
                date(year, *raeknakhwan_dates[year]), raeknakhwan
            )
        # Approx. otherwise for 1957-2013
        elif 1957 <= year <= 1996:
            _add_with_observed(date(year, MAY, 13), raeknakhwan)


class TH(Thailand):
    pass


class THA(Thailand):
    pass
