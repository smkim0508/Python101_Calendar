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


