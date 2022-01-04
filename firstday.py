from leapyear import numLeaps
from week_month_def import numDaysMonth

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
