"""
Tests for MOD4 exercises:
  ex00 - FileLoader
  ex01 - YoungestFellah
  ex02 - ProportionBySport
  ex03 - HowManyMedals
  ex04 - SpatioTemporalData
  ex05 - HowManyMedalsByCountry
  ex06 - MyPlotLib
  ex07 - Komparator

Run with:  python test_mod4.py
"""
import sys
import os
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

import importlib.util
_requires_scipy = unittest.skipUnless(
    importlib.util.find_spec("scipy") is not None, "scipy not installed"
)

BASE = os.path.dirname(os.path.abspath(__file__))
for _ex in ("ex00", "ex01", "ex02", "ex03", "ex04", "ex05", "ex06", "ex07"):
    sys.path.insert(0, os.path.join(BASE, _ex))

from FileLoader import FileLoader
from YoungestFellah import youngest_fellah
from ProportionBySport import proportion_by_sport
from HowManyMedals import how_many_medals
from SpatioTemporalData import SpatioTemporalData
from HowManyMedalsByCountry import how_many_medals_by_country
from MyPlotLib import MyPlotLib
from Komparator import Komparator

ATHLETE_CSV = os.path.join(BASE, "data", "athlete_events.csv")

# ── Shared synthetic athlete DataFrame ────────────────────────────────────
#
# Columns match athlete_events.csv:
# ID, Name, Sex, Age, Height, Weight, Team, NOC, Games, Year,
# Season, City, Sport, Event, Medal

_COLS = ["ID", "Name", "Sex", "Age", "Height", "Weight", "Team", "NOC",
         "Games", "Year", "Season", "City", "Sport", "Event", "Medal"]

_ROWS = [
    # Alice – individual swimmer, medals in two years
    (1, "Alice Star",   "F", 22, 165, 58, "USA", "USA", "2000 Summer", 2000, "Summer", "Sydney",  "Swimming",    "100m Free",                         "Gold"),
    (1, "Alice Star",   "F", 26, 165, 58, "USA", "USA", "2004 Summer", 2004, "Summer", "Athens",  "Swimming",    "100m Free",                         "Silver"),
    (1, "Alice Star",   "F", 26, 165, 58, "USA", "USA", "2004 Summer", 2004, "Summer", "Athens",  "Swimming",    "200m Free",                         "Gold"),
    # Bob – no medals
    (2, "Bob Runner",   "M", 19, 175, 70, "GBR", "GBR", "2000 Summer", 2000, "Summer", "Sydney",  "Athletics",   "100m Sprint",                       float("nan")),
    (2, "Bob Runner",   "M", 23, 175, 70, "GBR", "GBR", "2004 Summer", 2004, "Summer", "Athens",  "Athletics",   "100m Sprint",                       float("nan")),
    # Team sport: Basketball USA 2000 (two separate events)
    (3, "Charlie Hoop", "M", 25, 198, 95, "USA", "USA", "2000 Summer", 2000, "Summer", "Sydney",  "Basketball",  "Basketball Men's Basketball",        "Gold"),
    (4, "Dana Dunk",    "F", 23, 175, 70, "USA", "USA", "2000 Summer", 2000, "Summer", "Sydney",  "Basketball",  "Basketball Women's Basketball",      "Gold"),
    # Eve – another swimmer 2000, then athlete 2004
    (5, "Eve Splash",   "F", 20, 168, 60, "USA", "USA", "2000 Summer", 2000, "Summer", "Sydney",  "Swimming",    "200m Free",                         "Bronze"),
    (5, "Eve Splash",   "F", 24, 168, 60, "USA", "USA", "2004 Summer", 2004, "Summer", "Athens",  "Athletics",   "200m Sprint",                       float("nan")),
    # City/year coverage for SpatioTemporalData
    (6, "Frank Jump",   "M", 30, 180, 80, "FRA", "FRA", "1996 Summer", 1996, "Summer", "Atlanta", "Athletics",   "High Jump",                         float("nan")),
    (7, "Gina Lift",    "F", 28, 158, 55, "CHN", "CHN", "1996 Summer", 1996, "Summer", "Atlanta", "Weightlifting","Snatch",                           "Bronze"),
]


def _make_athletes():
    return pd.DataFrame(_ROWS, columns=_COLS)


# ── ex00: FileLoader ───────────────────────────────────────────────────────

class TestFileLoader(unittest.TestCase):
    def setUp(self):
        self.fl = FileLoader()
        self.df = _make_athletes()

    def test_load_real_csv_returns_dataframe(self):
        df = self.fl.load(ATHLETE_CSV)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(df.shape[0], 0)

    def test_load_real_csv_has_expected_columns(self):
        df = self.fl.load(ATHLETE_CSV)
        for col in ("Name", "Sex", "Age", "Year", "Medal"):
            self.assertIn(col, df.columns)

    def test_load_missing_file_returns_none(self):
        self.assertIsNone(self.fl.load("/no/such/file.csv"))

    def test_display_head_prints_rows(self):
        # Smoke-test: should not raise
        self.fl.display(self.df, 3)

    def test_display_tail_negative_n(self):
        self.fl.display(self.df, -2)

    def test_display_zero_does_nothing(self):
        self.fl.display(self.df, 0)

    def test_display_non_dataframe_does_not_raise(self):
        self.fl.display("not a df", 3)


# ── ex01: YoungestFellah ──────────────────────────────────────────────────

class TestYoungestFellah(unittest.TestCase):
    def setUp(self):
        self.df = _make_athletes()

    def test_returns_dict_with_f_and_m_keys(self):
        result = youngest_fellah(self.df, 2000)
        self.assertIsInstance(result, dict)
        self.assertIn("f", result)
        self.assertIn("m", result)

    def test_youngest_female_2000(self):
        # Females in 2000: Alice(22), Dana(23), Eve(20) → youngest = 20
        result = youngest_fellah(self.df, 2000)
        self.assertEqual(result["f"], 20)

    def test_youngest_male_2000(self):
        # Males in 2000: Bob(19), Charlie(25) → youngest = 19
        result = youngest_fellah(self.df, 2000)
        self.assertEqual(result["m"], 19)

    def test_year_with_no_participants_returns_nan(self):
        result = youngest_fellah(self.df, 1800)
        self.assertTrue(np.isnan(result["f"]))
        self.assertTrue(np.isnan(result["m"]))

    def test_year_2004_youngest_female(self):
        # Females in 2004: Alice(26), Eve(24) → youngest = 24
        result = youngest_fellah(self.df, 2004)
        self.assertEqual(result["f"], 24)


# ── ex02: ProportionBySport ───────────────────────────────────────────────

class TestProportionBySport(unittest.TestCase):
    def setUp(self):
        self.df = _make_athletes()

    def test_returns_float(self):
        p = proportion_by_sport(self.df, 2000, "Swimming", "F")
        self.assertIsInstance(p, float)

    def test_proportion_in_unit_interval(self):
        p = proportion_by_sport(self.df, 2000, "Swimming", "F")
        self.assertGreaterEqual(p, 0.0)
        self.assertLessEqual(p, 1.0)

    def test_swimming_females_2000(self):
        # Unique female athletes in 2000: Alice(Swimming), Dana(Basketball), Eve(Swimming)
        # After drop_duplicates on (Name, Sport): Alice/Swimming, Dana/Basketball, Eve/Swimming
        # Swimmers: 2 out of 3 → 2/3
        p = proportion_by_sport(self.df, 2000, "Swimming", "F")
        self.assertAlmostEqual(p, 2 / 3, places=9)

    def test_absent_sport_returns_zero(self):
        p = proportion_by_sport(self.df, 2000, "Archery", "M")
        self.assertEqual(p, 0.0)

    def test_nonexistent_year_returns_zero(self):
        p = proportion_by_sport(self.df, 1800, "Swimming", "F")
        self.assertEqual(p, 0.0)

    def test_sole_sport_for_gender_returns_one(self):
        # Only one male athlete in 2004 (Bob, Athletics)
        p = proportion_by_sport(self.df, 2004, "Athletics", "M")
        self.assertEqual(p, 1.0)


# ── ex03: HowManyMedals ───────────────────────────────────────────────────

class TestHowManyMedals(unittest.TestCase):
    def setUp(self):
        self.df = _make_athletes()

    def test_returns_dict(self):
        self.assertIsInstance(how_many_medals(self.df, "Alice Star"), dict)

    def test_alice_year_2000_gold(self):
        result = how_many_medals(self.df, "Alice Star")
        self.assertIn(2000, result)
        self.assertEqual(result[2000]["G"], 1)
        self.assertEqual(result[2000]["S"], 0)
        self.assertEqual(result[2000]["B"], 0)

    def test_alice_year_2004_gold_and_silver(self):
        result = how_many_medals(self.df, "Alice Star")
        self.assertIn(2004, result)
        self.assertEqual(result[2004]["G"], 1)
        self.assertEqual(result[2004]["S"], 1)
        self.assertEqual(result[2004]["B"], 0)

    def test_no_medal_athlete_all_counts_zero(self):
        result = how_many_medals(self.df, "Bob Runner")
        for year_data in result.values():
            self.assertEqual(year_data["G"], 0)
            self.assertEqual(year_data["S"], 0)
            self.assertEqual(year_data["B"], 0)

    def test_unknown_athlete_empty_dict(self):
        self.assertEqual(how_many_medals(self.df, "Nobody"), {})

    def test_medal_keys_always_present(self):
        result = how_many_medals(self.df, "Alice Star")
        for year_data in result.values():
            self.assertEqual(set(year_data.keys()), {"G", "S", "B"})

    def test_counts_are_integers(self):
        result = how_many_medals(self.df, "Alice Star")
        for year_data in result.values():
            for count in year_data.values():
                self.assertIsInstance(count, int)


# ── ex04: SpatioTemporalData ──────────────────────────────────────────────

class TestSpatioTemporalData(unittest.TestCase):
    def setUp(self):
        self.std = SpatioTemporalData(_make_athletes())

    def test_when_returns_list(self):
        self.assertIsInstance(self.std.when("Sydney"), list)

    def test_when_sydney_includes_2000(self):
        self.assertIn(2000, self.std.when("Sydney"))

    def test_when_sorted_descending(self):
        result = self.std.when("Atlanta")
        self.assertEqual(result, sorted(result, reverse=True))

    def test_when_unknown_city_empty(self):
        self.assertEqual(self.std.when("Narnia"), [])

    def test_where_returns_list(self):
        self.assertIsInstance(self.std.where(2000), list)

    def test_where_2000_includes_sydney(self):
        self.assertIn("Sydney", self.std.where(2000))

    def test_where_1996_includes_atlanta(self):
        self.assertIn("Atlanta", self.std.where(1996))

    def test_where_unknown_year_empty(self):
        self.assertEqual(self.std.where(1800), [])


# ── ex05: HowManyMedalsByCountry ──────────────────────────────────────────

class TestHowManyMedalsByCountry(unittest.TestCase):
    def setUp(self):
        self.df = _make_athletes()

    def test_returns_dict(self):
        self.assertIsInstance(how_many_medals_by_country(self.df, "USA"), dict)

    def test_usa_has_medals(self):
        result = how_many_medals_by_country(self.df, "USA")
        self.assertGreater(len(result), 0)

    def test_medal_dict_keys(self):
        result = how_many_medals_by_country(self.df, "USA")
        for year_data in result.values():
            self.assertEqual(set(year_data.keys()), {"G", "S", "B"})

    def test_counts_non_negative_ints(self):
        result = how_many_medals_by_country(self.df, "USA")
        for year_data in result.values():
            for count in year_data.values():
                self.assertIsInstance(count, int)
                self.assertGreaterEqual(count, 0)

    def test_team_basketball_event_counted_once(self):
        # Men's Basketball event → 1 Gold (not 1 per player)
        # Women's Basketball event → 1 Gold
        # Alice Swimming 2000 → 1 Gold; Eve Swimming 2000 → 1 Bronze
        # Total USA Gold in 2000: 1(Alice) + 1(Men's BB) + 1(Women's BB) = 3
        result = how_many_medals_by_country(self.df, "USA")
        self.assertIn(2000, result)
        self.assertEqual(result[2000]["G"], 3)
        self.assertEqual(result[2000]["B"], 1)

    def test_no_medal_country_all_zero(self):
        result = how_many_medals_by_country(self.df, "GBR")
        for year_data in result.values():
            self.assertEqual(year_data["G"], 0)
            self.assertEqual(year_data["S"], 0)
            self.assertEqual(year_data["B"], 0)

    def test_unknown_country_empty(self):
        self.assertEqual(how_many_medals_by_country(self.df, "ZZZ"), {})


# ── ex06: MyPlotLib ───────────────────────────────────────────────────────

def _numeric_df():
    np.random.seed(0)
    return pd.DataFrame({
        "Age":   np.random.randint(15, 45, 100).astype(float),
        "Height": np.random.normal(170, 10, 100),
        "Weight": np.random.normal(65, 12, 100),
        "Label": ["A"] * 50 + ["B"] * 50,
    })


class TestMyPlotLib(unittest.TestCase):
    def setUp(self):
        self.pl = MyPlotLib()
        self.df = _numeric_df()

    @patch("matplotlib.pyplot.show")
    def test_histogram_runs(self, _):
        self.pl.histogram(self.df, ["Age", "Height"])

    @patch("matplotlib.pyplot.show")
    def test_histogram_skips_non_numeric(self, _):
        self.pl.histogram(self.df, ["Label"])

    @_requires_scipy
    @patch("matplotlib.pyplot.show")
    def test_density_runs(self, _):
        self.pl.density(self.df, ["Height", "Weight"])

    @_requires_scipy
    @patch("matplotlib.pyplot.show")
    def test_density_single_feature(self, _):
        self.pl.density(self.df, ["Age"])

    @patch("matplotlib.pyplot.show")
    @patch("seaborn.pairplot")
    def test_pair_plot_runs(self, *_):
        self.pl.pair_plot(self.df, ["Age", "Height", "Weight"])

    @patch("matplotlib.pyplot.show")
    def test_box_plot_runs(self, _):
        self.pl.box_plot(self.df, ["Age", "Height"])

    @patch("matplotlib.pyplot.show")
    def test_box_plot_single_feature(self, _):
        self.pl.box_plot(self.df, ["Weight"])

    @patch("matplotlib.pyplot.show")
    def test_histogram_empty_numeric_list_does_not_raise(self, _):
        self.pl.histogram(self.df, [])


# ── ex07: Komparator ──────────────────────────────────────────────────────

def _binary_df():
    np.random.seed(1)
    return pd.DataFrame({
        "Group": ["X"] * 40 + ["Y"] * 40,
        "Score": np.concatenate([
            np.random.normal(50, 5, 40),
            np.random.normal(65, 8, 40),
        ]),
        "Value": np.concatenate([
            np.random.normal(100, 10, 40),
            np.random.normal(120, 15, 40),
        ]),
    })


class TestKomparator(unittest.TestCase):
    def setUp(self):
        self.df = _binary_df()

    @patch("matplotlib.pyplot.show")
    def test_compare_box_plots_runs(self, _):
        Komparator(self.df).compare_box_plots("Group", "Score")

    @_requires_scipy
    @patch("matplotlib.pyplot.show")
    def test_density_runs(self, _):
        Komparator(self.df).density("Group", "Score")

    @patch("matplotlib.pyplot.show")
    def test_compare_histograms_runs(self, _):
        Komparator(self.df).compare_histograms("Group", "Score")

    @patch("matplotlib.pyplot.show")
    def test_single_category_does_not_raise(self, _):
        df = pd.DataFrame({"Cat": ["A"] * 10, "Val": range(10)})
        Komparator(df).compare_box_plots("Cat", "Val")

    @patch("matplotlib.pyplot.show")
    def test_compare_box_plots_second_variable(self, _):
        Komparator(self.df).compare_box_plots("Group", "Value")

    @_requires_scipy
    @patch("matplotlib.pyplot.show")
    def test_density_second_variable(self, _):
        Komparator(self.df).density("Group", "Value")

    @patch("matplotlib.pyplot.show")
    def test_compare_histograms_second_variable(self, _):
        Komparator(self.df).compare_histograms("Group", "Value")


if __name__ == "__main__":
    unittest.main(verbosity=2)
