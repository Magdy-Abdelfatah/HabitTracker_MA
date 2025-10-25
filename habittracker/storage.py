# Storage to save and load data from JSON
"""
Handles saving and loading habits in JSON format.
Each profile (real or demo) has its own file.
"""
import json
import os
from habit import habit_from_dict

CURRENT_PROFILE = "real"
FILE_PATH = "habits.json"

def set_profile(profile):
    """Switch between real and demo profiles."""
    global CURRENT_PROFILE, FILE_PATH
    if profile == "demo":
        CURRENT_PROFILE = "demo"
        FILE_PATH = "demo_user_habits.json"
    else:
        CURRENT_PROFILE = "real"
        FILE_PATH = "habits.json"

def init_storage():
    """Make sure the JSON file exists."""
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file: #opens the file in "w" mode
            json.dump([], file) #creates the file with an empty list

def load_habits():
    """Load Habit from the JSON file."""
    try:
        with open(FILE_PATH, "r") as file: #opens the file in "r" mode
            data = json.load(file)
            return [habit_from_dict(item) for item in data]
    except:
        # If the file is missing or broken, start fresh
        save_habits([])
        return []

def save_habits(habits):
    """Saves Habits to the JSON file."""
    with open(FILE_PATH, "w") as file: #opens the file in "w" mode
        json.dump([h.to_dict() for h in habits], file, indent=2) #indent to split into 2 lines (easier overview)