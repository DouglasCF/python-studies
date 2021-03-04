def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


print(isLeapYear(2020))  # True
print(isLeapYear(2021))  # False
print(isLeapYear(2100))  # False
print(isLeapYear(2400))  # True
print(isLeapYear(800))  # True
