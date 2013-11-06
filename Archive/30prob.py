pow_dict = {}
for x in xrange(0,10):
    pow_dict[str(x)] = x**5

def fifth_pow_digit(x):
    x = str(x)
    total = 0
    for num in x:
        total += pow_dict[num]
    return total
    
sum = 0
for x in xrange(10,1000000):
    if fifth_pow_digit(x) == x:
        print x
        sum += x
        
print sum