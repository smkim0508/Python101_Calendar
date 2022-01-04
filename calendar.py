from attributes import dayOfMonth, spacing
from firstday import firstOfYear, firstOfYear2, firstOfMonth
from leapyear import isLeapYear, numLeaps
from print_calendar import printMonth
from suffix import daySuffix, daySuffix2
from week_month_def import numDaysMonth, monthOfYear, dayOfWeek
import re, string, sys, random

print("Welcome to the calendar program!")
print("")
print("If you provide a year only, you get a calendar for that year.")
print("If you provide a year and a month, you get a calendar for that month.")
print("If you provide a year, month, and date, you get the day of week of that day.")
print("")
print("First, please provide a year. (It can even be zero or negative.)")
print("")

needInput = True
while needInput:
    try:
        year = int(input("> "))
        needInput = False
    except ValueError:
        print("We need a number, please")
print("")
print("Now, if you like, provide a month as a number between 1 - 12")
print("Otherwise you'll get a year calendar instead.")
print("")
needinput = True
while needinput:
    try:
        month = input("> ")
        if month != "":
            month = int(month)
            if (month < 1):
                print("The month must be greater than zero")
            elif (month > 12):
                print("The month must be 12 or less")
            else:
                needinput = False
        else:
            needinput = False
    except ValueError:
        print("We need a number between 1 and 12, please")
if (month == ""):
    print(" -~--~- Calendar for " + str(year) + " -~--~-")
    for x in range (1,13):
        printMonth(x,year)
        print("")
else:
    monthstr = monthOfYear(month)
    numdays = numDaysMonth(month,year)
    print("")
    print("Now, if you like, privide a numerical day within " + monthstr + " (which has " + str(numdays) + " days),")
    print("to get the day of week of that day.")
    print("Otherwise you'll get a month calendar instead.")
    print("")
    needinput = True
    while needinput:
        try:
            day = input("> ")
            if day != "":
                day = int(day)
                if (day < 1):
                    print("The day must be greater than zero")
                elif (day > numdays):
                    print("The month must be " + str(numdays) + " or less")
                else:
                    needinput = False
            else:
                needinput = False
        except ValueError:
            print("We need a number between 1 and " + str(numdays) + ", please")
    if (day == ""):
        printMonth(month,year)
    else:
        daystr = dayOfWeek(dayOfMonth(day,month,year))
        print("The " + str(day) + daySuffix(day) + " of " + monthstr + ", " + str(year) + " is a " + daystr + ".")
