from datetime import datetime, timedelta

def calculate_full_weeks_and_extra_days(year):
    start_date = datetime(year, 9, 1)  # September 1st of the given year
    end_date = datetime(year + 1, 6, 1)  # June 1st of the following year

    # Find the first Monday on or after September 1st
    while start_date.weekday() != 0:
        start_date += timedelta(days=1)

    # Find the last Sunday on or before May 31st
    last_day = end_date - timedelta(days=1)
    while last_day.weekday() != 6:
        last_day -= timedelta(days=1)

    # Calculate the number of full weeks
    full_weeks = (last_day - start_date).days // 7

    # Calculate the extra days before the first full week
    extra_days_before = (start_date - datetime(year, 9, 1)).days

    # Calculate the extra days after the last full week
    extra_days_after = (datetime(year + 1, 6, 1) - last_day - timedelta(days=1)).days

    return full_weeks, extra_days_before, extra_days_after

# Example usage:
year = 2023  # Replace with the desired year
full_weeks, extra_days_before, extra_days_after = calculate_full_weeks_and_extra_days(year)
print(f"Full weeks: {full_weeks}")
print(f"Extra days before full weeks: {extra_days_before}")
print(f"Extra days after full weeks: {extra_days_after}")
