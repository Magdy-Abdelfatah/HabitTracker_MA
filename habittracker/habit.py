""""
Defines the Habit class for storing habit data in JSON format.
"""
from datetime import datetime

class Habit:
    """
    Represents a single habit with a name, periodicity ('daily' or 'weekly'),
    a creation date, and a list of completion dates (as 'YYYY-MM-DD' strings).
    """
    def __init__(self, name: str, periodicity: str, created_at=None, completions=None):
        """
        Initialize a new habit.
        Args:
            name (str): Name of the habit.
            periodicity (str): 'daily' or 'weekly'.
            created_at (str, optional): Date of creation in 'YYYY-MM-DD' format.
            completions (list[str], optional): List of completion dates.
        """
        self.name = name.strip()                     # remove unnecessary spaces
        self.periodicity = periodicity               # repetition type
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d")  # default = today
        self.completions = completions if completions is not None else []     # empty list if none given

    def add_completion(self, completion: str):
        """
        Add a completion date (as 'YYYY-MM-DD') to the habit history.
        """
        self.completions.append(completion)          # append to list

    def to_dict(self) -> dict:
        """
        Convert this Habit object into a dictionary for saving to JSON.
        Returns:
            dict: A plain dictionary version of the habit.
                  Matches the structure used in the JSON storage file.
        """
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at,
            "completions": self.completions,
        }

def habit_from_dict(data: dict) -> Habit:
    """
    Create a Habit object from a dictionary (used when loading from JSON).
    Args:
        data (dict): A dictionary containing habit data.
    Returns:
        Habit: A new Habit instance with the loaded data.
    """
    return Habit(
        name=data.get("name", ""),                   # default empty string if missing
        periodicity=data.get("periodicity", "daily"),# assume daily if not given
        created_at=data.get("created_at"),           # creation date
        completions=data.get("completions", []),     # list of completions
    )