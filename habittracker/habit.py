"""
Simple Habit class that works with JSON files.
"""
from datetime import datetime

class Habit:
    """Represents one habit with a name, periodicity (daily/weekly),
    creation date, and completion timestamps.
    """
    def __init__(self, name: str, periodicity: str, created_at=None, completions=None):
        self.name = name.strip()
        self.periodicity = periodicity
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d")
        self.completions = completions if completions is not None else []

    def add_completion(self, completion: str):
        """Add a completion timestamp."""
        self.completions.append(completion)

    def to_dict(self) -> dict:
        """Return a dictionary version for saving as JSON."""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at,
            "completions": self.completions,
        }

def habit_from_dict(data: dict) -> Habit:
    """Load a Habit object from dictionary data."""
    return Habit(
        name=data.get("name", ""),
        periodicity=data.get("periodicity", "daily"),
        created_at=data.get("created_at"),
        completions=data.get("completions", []),
    )