#!/usr/bin/env python3

DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def main():
    total_days = 1 # For calculating weekdays
    result = 0

    for year in range(1901, 2001):
        for month in range(12):
            if (total_days % 7 == 6): # Check
                result += 1

            if (month == 1) and ((year % 4 == 0) and (year % 400 != 0)): # Leap years
                total_days += 1

            total_days += DAYS_PER_MONTH[month] # Increment
            
    print(f"Matching Sundays: {result}")

if __name__ == "__main__":
    main()