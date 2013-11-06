months = [ 31 , 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [ 31 , 29 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year % 100 == 0:
        return (year / 400.0) == 0
    else:
        return (year / 4.0) == 0
    
# day of week is 0-6
day_of_week = 1
count = 0
for year in xrange(1900, 2001):
    for days in months_leap if is_leap(year) else months:
        day_of_week += days
        day_of_week %= 7
        if year != 1900 and day_of_week == 0:
            count += 1
print count