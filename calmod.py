import sys
import stdio

# function to determine leap year 
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

# function that gets the number of days in a month
def get_month_days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28

# gets the start date of the month using Zeller's Congruence
def get_start_day(month, year):
    if month < 3:
        month += 12
        year -= 1
        
    q = 1  # First day of the month
    m = month
    K = year % 100
    J = year // 100
    f = q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) + 5 * J
    h = f % 7
    
    # Convert result to make Monday = 0, Tuesday = 1, ... Sunday = 6
    return (h - 2) % 7

# function to print the calendar
def print_calendar(month, year):
    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    month_days = get_month_days(month, year)
    start_day = get_start_day(month, year)

    stdio.write(" ".join(days) + '\n')
    for i in range(start_day):
        stdio.write('   ')

    for day in range(1, month_days + 1):
        stdio.writef('%2d ', day)
        if (day + start_day) % 7 == 0:
            stdio.write('\n')
    if (day + start_day) % 7 != 0:
        stdio.write('\n')


