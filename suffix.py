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
