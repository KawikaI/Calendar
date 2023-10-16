# almost finished
# convert to stdio standards
# claim functions

import stdio

# function to determine leap year 
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

# function that gets the number of days in a month
def get_month_days(month, year):
    # list of months that have 31 days
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # list of months that have 30 days
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        # returns 29 if leap year, else returns 28
        return 29 if is_leap(year) else 28


# gets the start date of the month
def get_start_day(month, year):
    # if month is jan or feb, subtract 1 from year
    if month < 3:
        month += 12
        year -= 1
    # 
    a = 1
    # sets b to the remainder of year divided by 100
    b = year % 100
    # sets c to the year divided by 100
    c = year // 100
    # formula to get the start day
    d = a + ((13 * (month + 1)) // 5) + b + (b // 4) + (c // 4) - (2 * c)
    # returns the start day
    return d % 7

# function to print the calendar
def print_calendar(month, year):
    # list of days
    days = ["Sa", "Su", "Mo", "Tu", "We", "Th", "Fr"]
    # sets the var to the function call of gwt_month_days
    month_days = get_month_days(month, year)
    # sets the var to the function call of get_start_day
    start_day = get_start_day(month, year)
    
    # prints the days of the week
    print("Mo Tu We Th Fr Sa Su")
    for i in range((start_day + 1) % 7):
        print("   ", end="")

    # prints the nums correlated with the days
    for day in range(1, month_days + 1):
        print(f"{day:2} ", end="")
        if (day + start_day) % 7 == 6:
            print()

if __name__ == "__main__":
    # input
    m = int(input("Enter the month (1-12): "))
    y = int(input("Enter the year (e.g., 2023): "))
    
    # prints the calendar
    print_calendar(m, y)
    
