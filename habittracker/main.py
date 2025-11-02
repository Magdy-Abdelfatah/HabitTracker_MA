# main.py
"""
Simple command-line Habit Tracker (skeleton version).

Profiles (separate JSON files):
- Real user  -> habits.json
- Demo user  -> demo_user_habits.json

Rules:
- Daily: one check-off per calendar day
- Weekly: one check-off per ISO week
- No future dates
"""

from habittracker.time_utils import parse_iso
from datetime import datetime
from habittracker.storage import init_storage, set_profile, load_habits
from habittracker.domain import add_habit, delete_habit, check_off, predefined_habits
from habittracker.analytics import (
    list_all_habits, list_by_periodicity,
    streak_summary_for, longest_daily_streak, longest_weekly_streak
)

def pause():
    """Wait for user to press ENTER before continuing."""
    # Used after showing lists or analytics
    pass


def choose_profile():
    """Ask the user which profile to use."""
    # set_profile("real") or set_profile("demo") from storage.py
    pass


def choose_periodicity():
    """Ask if the habit is daily or weekly."""
    # returns "daily" or "weekly"
    pass


def show_habits(habits):
    """Print all habits with index numbers."""
    # uses load_habits() from storage.py
    pass


def choose_check_date():
    """Ask when to check off (today or custom date)."""
    # uses parse_iso() from time_utils.py
    pass


def run():
    """Main menu loop."""
    # init_storage() → sets up files
    # load_habits() → gets all saved habits
    # add_habit(), delete_habit(), check_off() → from domain.py
    # list_all_habits(), list_by_periodicity() → from analytics.py
    pass

if __name__ == "__main__":
    run()