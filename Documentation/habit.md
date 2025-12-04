# habit.py Documentation

## Overview
The Habit class defines the structure of a habit object.  
All habits are stored as JSON and reloaded into this class when the program runs.

## Attributes
- name  
- periodicity (daily/weekly)  
- created_at (YYYY-MM-DD)  
- completions (list of ISO timestamps)

## Key Components

### __init__(...)
Initializes a habit.  
Defaults:
- created_at → today  
- completions → empty list

### add_completion(date_string)
Adds a new completion date.

### to_dict()
Converts the habit to a dictionary for JSON storage.

### habit_from_dict()
Creates a Habit instance from JSON-loaded data.