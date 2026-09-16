# ZuberiDaley_Glab-385.5.1.py
# Guided Lab 385.5.1 - Convert Between Two Specific Time Zones

# Prerequisite: pip install pytz

from datetime import datetime
import pytz


# Define a function to convert a datetime object between two time zones
def convert_time_zone(dt, from_tz, to_tz):
    """
    Converts a datetime object from one time zone to another.

    Args:
        dt (datetime): The datetime object to convert.
        from_tz (str): The current time zone of the datetime object.
        to_tz (str): The time zone to convert the datetime object to.

    Returns:
        datetime: The converted datetime object.
    """
    # Create timezone objects
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)

    # Convert the datetime object to the 'from_tz' timezone (if necessary)
    dt = dt.replace(tzinfo=from_tz)

    # Convert the datetime object to the 'to_tz' timezone
    dt = dt.astimezone(to_tz)

    return dt


# Example: convert 2022-01-01 12:30:45 from UTC to New York time

# Define a datetime object
dt = datetime(2022, 1, 1, 12, 30, 45)

# Define the current time zone of the datetime object
from_tz = "UTC"

# Define the time zone to convert the datetime object to
to_tz = "America/New_York"

# Convert the datetime object between the two time zones
converted_dt = convert_time_zone(dt, from_tz, to_tz)

# Print the converted datetime object
print(converted_dt)
