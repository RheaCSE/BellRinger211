import datetime

current_time = datetime.datetime.now()
valentines_day = datetime.datetime(2025, 2, 14)

time_difference = valentines_day - current_time
hours_until_valentines = time_difference.total_seconds() / 3600


print(f"Current time: {current_time}")
print(f"Hours until Valentine's Day 2025: {hours_until_valentines:.0f} hours")

if current_time.month == 2 and current_time.day == 14:
    print("Happy Valentine's Day!")
