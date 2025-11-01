# Functions used by the CLI (main.py)

from habittracker.habit import Habit
from habittracker.storage import load_habits, save_habits
from datetime import datetime
from habittracker.time_utils import daily_key, weekly_key, to_iso, parse_iso


def is_future(date_object):
    """Return True if the given date is in the future."""
    return date_object > datetime.now()

def add_habit(name, periodicity):
    """Add a new habit if it doesn’t already exist."""
    name = name.strip()
    if len(name) == 0:
        return False
    habits = load_habits()
    for h in habits:
        if h.name.lower() == name.lower():
            return False
    habits.append(Habit(name, periodicity))
    save_habits(habits)
    return True


def predefined_habits():
    """Return a list of predefined habits for quick adding."""
    return [
        {"name": "Drink 4L Water", "periodicity": "daily"},
        {"name": "Learn Python 30 minutes", "periodicity": "daily"},
        {"name": "Yoga 30 minutes", "periodicity": "daily"},
        {"name": "Deep Clean", "periodicity": "weekly"},
        {"name": "Call parents", "periodicity": "weekly"},
    ]


def delete_habit(name):
    """Remove a habit by its name. Returns True if deleted."""
    habits = load_habits()
    new_list = [h for h in habits if h.name != name]  # keep everything except the one to delete

    if len(new_list) == len(habits):  # nothing was removed
        return False

    save_habits(new_list)
    return True


def check_off(name, when_dt=None):
    """
    Mark a habit as completed.
    Rules:
    - Daily: only once per calendar day
    - Weekly: only once per ISO week
    - No future dates allowed
    """
    habits = load_habits()
    name_key = name.strip().lower()

    # find the matching habit
    target = None
    for h in habits:
        if h.name.lower() == name_key:
            target = h
            break

    if target is None:
        return False, "Habit not found."

    when_dt = when_dt or datetime.now()

    # prevent checking off in the future
    if is_future(when_dt):
        return False, "Cannot check off in the future."

    when_iso = to_iso(when_dt)  # format date as 'YYYY-MM-DD'

    # block check-offs before habit was created
    created_date = parse_iso(target.created_at).date()  # convert string to date
    if when_dt.date() < created_date:
        return False, f"Cannot check off before the habit was created ({target.created_at})."

    # check for duplicates in same day/week
    if target.periodicity == "daily":
        new_day = daily_key(when_iso)
        for ts in target.completions:
            if daily_key(ts) == new_day:
                return False, f"'{target.name}' is already checked off for {when_iso}."
    else:
        new_week = weekly_key(when_iso)
        for ts in target.completions:
            if weekly_key(ts) == new_week:
                y, w = new_week
                return False, f"'{target.name}' is already checked off for week {y}-W{str(w).zfill(2)}."

    # record the new completion and save
    target.add_completion(when_iso)
    save_habits(habits)
    return True, f"Checked off '{target.name}' for {when_iso}."