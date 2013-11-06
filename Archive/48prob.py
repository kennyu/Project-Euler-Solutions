
div_last_ten_digits = 10**10

count = 0
for x in xrange(1, 1001):
    count += x**x
    count %= div_last_ten_digits
    
print count