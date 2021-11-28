#!/usr/bin/env python3

### Euler Problem 19
# 1 Jan 1900 was a Monday.
    # Thirty days has September,
    # April, June and November.
    # All the rest have thirty-one,
    # Saving February alone,
    # Which has twenty-eight, rain or shine.
    # And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

### Globals
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] # Just for printing
DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

### Main
def main():
    total_days = 1 # For calculating weekdays
    result = 0

    for year in range(1901, 2001):
        for month in range(12):
            # Check
            weekday = total_days % 7 # DEBUG
            weekday_str = WEEKDAYS[weekday] # DBUG
            if (weekday == 6):
                print(f"{WEEKDAYS[weekday]}, 1/{month + 1}/{year}\t\tMatch?\tYES") # Match found!
                result += 1
            else: print(f"{WEEKDAYS[weekday]}, 1/{month + 1}/{year}\t\tMatch?\tNO")

            # Increment (Handling Feb)
            total_days += DAYS_PER_MONTH[month]
            if (month == 1) and ((year % 4 == 0) and (year % 400 != 0)):
                total_days += 1
            
    print(f"The number of Sundays that fell on first of the month was: {result}")



if __name__ == "__main__":
    main()