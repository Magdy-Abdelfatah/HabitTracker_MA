"""
Handles saving and loading habits in JSON format.
Each profile (real or demo) uses its own file.
"""
import json
import os
from habittracker.habit import habit_from_dict

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
REAL_FILE = os.path.join(PROJECT_ROOT, "habits.json")
DEMO_FILE = os.path.join(PROJECT_ROOT, "demo_user_habits.json")
TEST_FILE = os.path.join(PROJECT_ROOT, "test_habits.json")
FILE_PATH = REAL_FILE

def use_test_file():
    """Switch to a separate JSON file used only for testing."""
    global FILE_PATH
    FILE_PATH = TEST_FILE

def set_profile(profile):
    """Switch between real and demo profiles."""
    global FILE_PATH
    FILE_PATH = DEMO_FILE if profile == "demo" else REAL_FILE

def init_storage():
    """
    Create the JSON file if it does not exist.
    """
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file:
            json.dump([], file)  # start with an empty list

def load_habits():
    """
    Load all habits from the JSON file.
    Returns a list of Habit objects.
    """
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)  # read JSON data
            return [habit_from_dict(item) for item in data]  # convert dicts to Habit objects
    except:
        # If the file is missing or broken, create a new empty file
        save_habits([])
        return []

def save_habits(habits):
    """
    Save all habits to the JSON file.
    """
    with open(FILE_PATH, "w") as file:
        json.dump([h.to_dict() for h in habits], file, indent=2)  # indent=2 makes it easier to read