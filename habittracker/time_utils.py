"""
Helpers for ISO timestamps and grouping by day/week.
All dates use ISO format: YYYY-MM-DD
"""
from datetime import datetime

ISO_FORMAT = "%Y-%m-%d"

def parse_iso(iso_timestamp):
    """Turn a text date like '2025-09-01' into a datetime object."""
    return datetime.strptime(iso_timestamp, ISO_FORMAT)

def to_iso(date_time):
    """Turn a datetime object into text format 'YYYY-MM-DD'."""
    return date_time.strftime(ISO_FORMAT)

def daily_key(iso_timestamp):
    """Return (year, month, day) for daily grouping."""
    date_obj = parse_iso(iso_timestamp)
    return (date_obj.year, date_obj.month, date_obj.day)

def weekly_key(iso_timestamp):
    """Return (ISO year, ISO week) for weekly grouping."""
    date_obj = parse_iso(iso_timestamp)
    iso_year, iso_week, _ = date_obj.isocalendar()
    return (iso_year, iso_week)