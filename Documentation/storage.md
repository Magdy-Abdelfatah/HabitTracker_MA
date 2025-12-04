# storage.py Documentation

## Overview
The storage.py module manages saving and loading habit data from JSON files.  
It also supports switching between:
- real user profile  
- demo profile  
- test profile (used for pytest)

## Responsibilities
- Persist habits as JSON
- Load habits from JSON into Habit objects
- Create missing storage files
- Switch active profile

## Key Components

### FILE_PATH and Profiles
Depending on active mode, data is stored in:
- habits.json  
- demo_user_habits.json  
- test_habits.json  

### set_profile(profile)
Switches between real and demo files.

### use_test_file()
Switches to test_habits.json for test execution.

### init_storage()
Creates the JSON file if it does not exist.

### load_habits()
Reads JSON and converts dictionaries into Habit objects via:
- habit_from_dict()

### save_habits(habits)
Writes all habit objects into the JSON file using:
- to_dict()  