from math import factorial
from itertools import count

sum =0

fact = {}
for f in xrange(10):
    fact[str(f)] = factorial(f)

def curious(num):   
    total = 0
    for elem in str(num): 
        total += fact[elem] 
    return total
    
for c in count(10):
    if c > 1000000:
       break
    sum += c if curious(c) == c else 0
    
print sum

