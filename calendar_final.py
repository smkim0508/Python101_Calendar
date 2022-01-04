import re, string, sys, random

def isLeapYear(year) :
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

def dayOfWeek(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    else:
        return "Invalid day"

def monthOfYear(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
    else:
        return "Invalid month"

def numDaysMonth(month,year):
    if month == 1:
        return 31
    elif month == 2:
        if (isLeapYear(year)):
            return 29
        else:
            return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31
    else:
        return "Not a month"

def daySuffix(day):
    if (day > 3) and (day < 21):
        return "th"
    elif (day > 31):
        return "invalid day"
    elif (day == 1) or (day == 21) or (day == 31):
        return "st"
    elif (day == 2) or (day == 22):
        return "nd"
    elif (day == 3) or (day == 23):
        return "rd"
    else:
        return "th"

def daySuffix2(day):
    day = abs(day)
    lastDigit = day % 10
    secondLastDigit = (day // 10) % 10
    if secondLastDigit == 1:
        return "th"
    elif lastDigit == 1:
        return "st"
    elif lastDigit == 2:
        return "nd"
    elif lastDigit == 3:
        return "rd"
    else:
        return "th"

def numLeaps(y1,y2):
    leapsfound = 0
    if (y1 == y2):
        return leapsfound
    elif (y1 < y2):
        low = y1
        high = y2
        neg = False
    else:
        low = y2
        high = y1
        neg = True
    for x in range(low,high):
        if (isLeapYear(x)):
            leapsfound = leapsfound + 1
    if neg:
        leapsfound = -1 * leapsfound

    return leapsfound


def firstOfYear(year):
    startday = 1
    if (year == 1):
        return startday
    else:
        leaps = numLeaps(1,year)
        day = (startday + leaps + year - 1) % 7
        return day

def firstOfYear2(year): # simplified version
        return (year + numLeaps(1,year)) % 7

def firstOfMonth(month,year):
    day = firstOfYear(year)
    if month == 1:
        return day
    else:
        for m in range(1,month):
            day = day + numDaysMonth(m,year)
    return day % 7

def dayOfMonth(day,month,year):
    daynum = firstOfMonth(month,year)
    return (daynum + day - 1) % 7

def spacing(num):
    if len(str(num)) == 1:
        return "  "
    else:
        return " "

def printMonth(month,year):
    monthstr = monthOfYear(month)
    print(" -~- Calendar for " + monthstr + ", " + str(year) + " -~-")
    print(" Su Mo Tu We Th Fr Sa")
    firstday = firstOfMonth(month,year)
    numdays = numDaysMonth(month,year)
    dayOfWeek = firstday
    for x in range(0,firstday):
        print("   ",end="")
    for date in range(1,numdays+1):
        print(spacing(date)+str(date),end="")
        dayOfWeek = (dayOfWeek+1)%7
        if ((dayOfWeek == 0) or date == numdays):
            print()

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



