from datetime import date

def list_all_habits(habits):
    """Return (name, periodicity) pairs for display."""
    return [(h.name, h.periodicity) for h in habits]

def list_by_periodicity(habits, period):
    """Return habits filtered by 'daily' or 'weekly'."""
    return [h for h in habits if h.periodicity == period]

def daily_runs(day_keys):  #validation
    """
    Count daily runs.
    Returns: (current_run, longest_run, total_streaks)
    Rule: 7 consecutive days = 1 streak.
    """
    if not day_keys:
        return 0, 0, 0
    days = sorted(set(day_keys)) # deduplicate + sort
    current_run = 1
    longest_run = 1
    total_streaks = 0
    for i in range(1, len(days)):
        prev_day= date(*days[i - 1]) # Date prev_day = date(2025, 5, 1)
        curr_day = date(*days[i]) # Date curr_day = date(2025, 5, 2)
        if (curr_day - prev_day).days == 1:   # To calculate if the current day exactly 1 day after previous 1
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            total_streaks += current_run // 7  # count full 7-day streaks
            current_run = 1

    total_streaks += current_run // 7
    return current_run, longest_run, total_streaks

def weekly_runs(week_keys): #validation
    """
    Count weekly runs.
    Returns: (current_run, longest_run, total_streaks)
    Rule: 2 consecutive ISO weeks = 1 streak.
    """
    if not week_keys:
        return 0, 0, 0
    weeks = sorted(week_keys)  # deduplicate + sort
    def next_week(y, w):
        return (y, w + 1) if w < 53 else (y + 1, 1)
    current_run = 1
    longest_run = 1
    total_streaks = 0
    for i in range(1, len(weeks)):
        prev_week = weeks[i - 1]
        curr_week = weeks[i]
        if curr_week == next_week(*prev_week):
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            total_streaks += current_run // 2  # cunt full 2-week streaks
            current_run = 1
    total_streaks += current_run // 2
    return current_run, longest_run, total_streaks