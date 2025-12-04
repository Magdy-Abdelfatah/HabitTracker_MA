# analytics.py Documentation

## Overview
The analytics.py module contains functions that analyze habit data, including streak calculations and filtered listings.

## Responsibilities
- Provide summaries for displaying habits
- Compute streaks for daily and weekly habits
- Identify longest streaks across all habits

## Key Functions

### list_all_habits(habits)
Returns a list of (name, periodicity) pairs.

### list_by_periodicity(habits, period)
Filters habits into daily or weekly subsets.

### daily_runs(day_keys)
Computes both:
- current streak  
- longest streak  

based on consecutive calendar days.

### weekly_runs(week_keys)
Computes streaks using ISO week numbers.

### streak_summary_for(habit)
Returns a streak overview for a single habit:
- type  
- current streak  
- longest streak  
- unit (days or weeks)

### longest_daily_streak(habits)
Returns longest streak among all daily habits.

### longest_weekly_streak(habits)
Returns longest streak among all weekly habits.