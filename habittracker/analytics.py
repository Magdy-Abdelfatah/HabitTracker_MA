
from datetime import date
from time_utils import daily_key, weekly_key

def list_all_habits(habits):
    """Return (name, periodicity) pairs for simple listing."""
    return [(h.name, h.periodicity) for h in habits]

def list_by_periodicity(habits, period):
    """Filter habits by 'daily' or 'weekly'."""
    return [h for h in habits if h.periodicity == period]

def daily_runs(day_keys):
    """
    Count consecutive-day runs for daily habits.
    Returns (current_run, longest_run), both measured in days.
    day_keys is a list of (Y, M, D) tuples.
    """
    if not day_keys:
        return 0, 0, 0

    days = sorted(day_keys)  # ensure chronological order
    current_run = 1          # at least the first day counts as a run of 1
    longest_run = 1

    # Walk through the days and check if each day follows the previous by exactly 1 day
    for i in range(1, len(days)):
        prev_day = date(*days[i - 1])
        curr_day = date(*days[i])
        if (curr_day - prev_day).days == 1:
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            # gap → run breaks and starts again with this day
            current_run = 1

    return current_run, longest_run

def weekly_runs(week_keys):
    """
    Count consecutive-week runs for weekly habits (ISO weeks).
    Returns (current_run, longest_run), both measured in weeks.
    week_keys is a list of (ISO_year, ISO_week) tuples.
    """
    if not week_keys:
        return 0, 0
    weeks = sorted(week_keys)
    # Next ISO week helper (handles week 53 → week 1 of next year)
    def next_week(y, w):
        return (y, w + 1) if w < 53 else (y + 1, 1)
    current_run = 1
    longest_run = 1
    for i in range(1, len(weeks)):
        prev_week = weeks[i - 1]
        curr_week = weeks[i]
        if curr_week == next_week(*prev_week):
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            current_run = 1
    return current_run, longest_run

def streak_summary_for(habit):
    """
    Build a small summary for one habit using consecutive streak rules.
    - Daily: count consecutive days
    - Weekly: count consecutive ISO weeks
    Returns a dict {type, current_streak, longest_streak, unit}.
    """
    if habit.periodicity == "daily":
        keys = [daily_key(ts) for ts in habit.completions]
        current_run, longest_run = daily_runs(keys)
        return {
            "type": "daily",
            "current_streak": current_run,
            "longest_streak": longest_run,
            "unit": "days",
        }
    else:
        keys = [weekly_key(ts) for ts in habit.completions]
        current_run, longest_run = weekly_runs(keys)
        return {
            "type": "weekly",
            "current_streak": current_run,
            "longest_streak": longest_run,
            "unit": "weeks",
        }