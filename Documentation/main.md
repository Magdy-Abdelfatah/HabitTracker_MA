# main.py Documentation

## Overview
The main.py file provides the command-line interface (CLI) for the Habit Tracker.  
It handles all user interactions: selecting a profile, viewing habits, adding and deleting habits, checking off progress, and displaying analytic insights such as streaks.  
All data processing and business logic is delegated to modules inside the habittracker package (domain, storage, analytics, and time_utils).

## Responsibilities
- Display menu navigation
- Handle user input
- Call domain logic functions such as adding/removing habits
- Call analytic functions for streak calculations

## Key Components

### pause()
Pauses the program until the user presses ENTER.  
Used after displaying lists or results.

### choose_profile()
Allows the user to select:
- real profile (habits.json)
- demo profile (demo_user_habits.json)

Uses:
- set_profile() from storage.py

### choose_periodicity()
Asks user whether the habit is:
- daily  
- weekly  

Returns a string accordingly.

### show_habits(habits)
Displays a numbered list of habits.  
Used before deleting or checking off a habit.

### choose_check_date()
Allows user to check off:
- today  
- a custom date  
- Not before creation 

Uses:
- parse_iso() from time_utils.py

### run()
Main menu loop:
- Prints welcome screen
- Loads profile and initializes storage
- Displays command options (list, add, delete, check off, streaks)
- Executes appropriate functions from:
  - domain.py  
  - analytics.py  
  - storage.py  

Program exits when the user chooses "0".

