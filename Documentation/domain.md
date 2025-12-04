# domain.py Documentation

## Overview
The domain.py file contains the core business logic of the Habit Tracker.  
It manages creating, validating, updating, and checking off habits.  
It interacts directly with the storage module to read and write habit data.

## Responsibilities
- Add new habits
- Provide predefined habits
- Delete habits
- Validate check-offs (no duplicates, no future dates)
- Enforce streak rules (daily & weekly)

## Key Functions

### is_future(date_object)
Returns True if a given datetime is in the future.

### add_habit(name, periodicity)
Creates a new habit, unless:
- name is empty
- a habit with that name already exists

Uses:
- load_habits()  
- save_habits()  
- Habit class

### predefined_habits()
Returns a list of sample habits for quick adding and testing.

### delete_habit(name)
Deletes a habit by name.  
Returns False if the habit does not exist.

### check_off(name, when_dt=None)
Core completion logic:
- Prevents checking off before creation date
- Prevents duplicate check-offs within same period
- Prevents future dates
- Converts datetime to ISO string
- Saves updated habit data
