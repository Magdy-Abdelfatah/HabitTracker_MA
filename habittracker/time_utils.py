"""
Helper functions for working with dates in ISO format.
All dates are represented as 'YYYY-MM-DD' strings.
"""
from datetime import datetime

ISO_FORMAT = "%Y-%m-%d"

def parse_iso(iso_timestamp: str) -> datetime:
    """
    Convert an ISO date string ('YYYY-MM-DD') into a datetime object.
    Args:
        iso_timestamp (str): A date string in ISO format.
    Returns:
        datetime: A datetime object representing the given date.
    """
    return datetime.strptime(iso_timestamp, ISO_FORMAT)

def to_iso(date_time: datetime) -> str:
    """
    Convert a datetime object into an ISO date string ('YYYY-MM-DD').
    Args:
        date_time (datetime): A datetime object.
    Returns:
        str: The date as an ISO string.
    """
    return date_time.strftime(ISO_FORMAT)

def daily_key(iso_timestamp: str) -> tuple[int, int, int]:
    """
    Extract (year, month, day) as a tuple from an ISO date string.
    Args:
        iso_timestamp (str): A date string in ISO format.
    Returns:
         A tuple like (2025, 9, 3).
         Used for comparing and grouping daily habits.
    """
    date_obj = parse_iso(iso_timestamp)
    return (date_obj.year, date_obj.month, date_obj.day)

def weekly_key(iso_timestamp: str) -> tuple[int, int]:
    """
    Extract (iso_year, iso_week) as a tuple from an ISO date string.
    Args:
        iso_timestamp (str): A date string in ISO format.
    Returns:
        tuple[int, int]: A tuple like (2025, 36) representing ISO year and week number.
                         Used for comparing and grouping weekly habits.
    """
    date_obj = parse_iso(iso_timestamp)
    iso_year, iso_week, _ = date_obj.isocalendar()
    return (iso_year, iso_week)