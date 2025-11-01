"""
Simple tests for the main Habit Tracker functions.
Covers habit creation, completion, future checks, and streak analytics.
"""

from datetime import datetime, timedelta
from habittracker import storage
from habittracker.domain import check_off
from habittracker.habit import Habit
from habittracker.analytics import (
    streak_summary_for,
    longest_daily_streak,
    longest_weekly_streak,
)


storage.use_test_file()
storage.init_storage()

def test_habit_creation():
    """Check that a new habit is created correctly."""
    h = Habit("Go for a walk", "daily")
    assert h.name == "Go for a walk"
    assert h.periodicity == "daily"
    assert h.completions == []


def test_add_completion():
    """Check that completions are added correctly."""
    h = Habit("Read a book", "daily")
    h.add_completion("2025-10-01")
    assert h.completions == ["2025-10-01"]


def test_check_off_future_date(tmp_path):
    """Future dates should not be allowed when checking off."""
    storage.save_habits([Habit("Do yoga", "daily")])
    future = datetime.now() + timedelta(days=1)
    ok, msg = check_off("Do yoga", when_dt=future)
    assert not ok
    assert "future" in msg.lower()


def test_daily_streak_summary():
    """Daily streak summary should return correct values."""
    completions = [f"2025-10-{str(i).zfill(2)}" for i in range(1, 8)]
    h = Habit("Drink water", "daily", "2025-10-01", completions)
    s = streak_summary_for(h)
    assert s["type"] == "daily"
    assert s["current_streak"] == 7
    assert s["longest_streak"] == 7
    assert s["unit"] == "days"


def test_weekly_streak_summary():
    """Weekly streak summary should return correct values."""
    completions = ["2025-10-01", "2025-10-08", "2025-10-15"]
    h = Habit("Clean the kitchen", "weekly", "2025-09-25", completions)
    s = streak_summary_for(h)
    assert s["type"] == "weekly"
    assert s["current_streak"] == 3
    assert s["longest_streak"] == 3
    assert s["unit"] == "weeks"


def test_longest_daily_streak():
    """Find the daily habit with the longest streak."""
    h1 = Habit("Read", "daily", completions=["2025-10-01", "2025-10-02", "2025-10-03"])
    h2 = Habit("Meditate", "daily", completions=["2025-10-01"])
    best_name, best_streak, unit = longest_daily_streak([h1, h2])
    assert best_name == "Read"
    assert isinstance(best_streak, int)
    assert unit == "days"


def test_longest_weekly_streak():
    """Find the weekly habit with the longest streak."""
    h1 = Habit("Laundry", "weekly", completions=["2025-09-01", "2025-09-08", "2025-09-15"])
    h2 = Habit("Grocery shopping", "weekly", completions=["2025-09-01"])
    best_name, best_streak, unit = longest_weekly_streak([h1, h2])
    assert best_name == "Laundry"
    assert isinstance(best_streak, int)
    assert unit == "weeks"