# takes 2 command line args and m and y and writes the monthly calendar of the mth month o year, 
import sys
import stdio

# function to determine leap year
def leap_year(year):
    year = int(sys.argv[1])
    isLeapYear = (year % 4 == 0)
    isLeapYear = isLeapYear and ((year % 100) != 0)
    isLeapYear = isLeapYear or ((year % 400) == 0)
    stdio.writeln(isLeapYear)

# function to determine the number of days in a month
def days_in_month(month, year):
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    if month == 4 or month == 6 or month == 9 or month == 11:
        stdio.writeln(30)
    elif month == 2:
        if leap_year(year):
            stdio.writeln(29)
        else:
            stdio.writeln(28)
    else:
        stdio.writeln(31)



def main():
    days_in_month(int(sys.argv[1]), int(sys.argv[2]))
if __name__ == '__main__':
    main()

