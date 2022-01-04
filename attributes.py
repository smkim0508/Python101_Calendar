from firstday import firstOfMonth

def dayOfMonth(day,month,year):
    daynum = firstOfMonth(month,year)
    return (daynum + day - 1) % 7

def spacing(num):
    if len(str(num)) == 1:
        return "  "
    else:
        return " "
        