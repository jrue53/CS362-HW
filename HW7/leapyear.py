def ly(year):
    leapyear = "This is a leap year"
    nleapyear = "This is not a leap year"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return leapyear
            else:
                return nleapyear
        else:
            return leapyear
    else:
        return nleapyear