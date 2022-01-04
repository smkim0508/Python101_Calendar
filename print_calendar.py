from firstday import firstOfMonth
from week_month_def import numDaysMonth
from week_month_def import monthOfYear
from attributes import spacing

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