def ly(year):
    leapyear = "This is a leap year"
    nleapyear = "This is not a leap year"
    if year % 4 == 0:
        if year % 100 == 0:
            return nleapyear
        else:
            return leapyear
    else:
        return nleapyear