# time_utils.py Documentation

## Overview
The time_utils.py module provides helper functions for handling dates in the Habit Tracker.  
All dates follow the standardized ISO format (`YYYY-MM-DD`) to ensure consistency across storage, analytics, and user input.

## Responsibilities
- Convert ISO date strings into datetime objects  
- Convert datetime objects back into ISO strings  
- Extract components used for streak logic (daily and weekly grouping)

## Key Functions

### parse_iso(iso_timestamp)
Converts a date string in ISO format into a datetime object.  
Used whenever input needs to be validated or compared.

### to_iso(date_time)
Returns the ISO-formatted string for a given datetime object.  
Ensures uniform saving and displaying of dates.

### daily_key(iso_timestamp)
Extracts a (year, month, day) tuple from an ISO date.  
Used for grouping and comparing daily completions.

### weekly_key(iso_timestamp)
Extracts (iso_year, iso_week) using ISO calendar conventions.  
Used for weekly streak calculations and preventing duplicate weekly check-offs.