from eulertools import prime_factors, primes
from itertools import product, combinations_with_replacement
from operator import mul

prime_list = primes(4000)
prime_set  = set(prime_list)
def is_abundant(x):
    if x in prime_set:
        return False
    factors = list(prime_factors(x, prime_list))
    primes = map( lambda x: x[0] , factors)
    expons = map( lambda x: x[1] , factors)
    sum = 0
    for p in product( *map(lambda x: range(x+1), expons)):
        if expons != list(p):
            sum += reduce( mul , map( lambda x, y: x**y , primes, p), 1)
    return sum > x
        

# find all abundant numbers less than or equal 28123

abundant_nums = []
for x in xrange(12,28124):
    if is_abundant(x):
        abundant_nums.append(x)

a = set(range(1,28124))
b = set([ x+y for x,y in combinations_with_replacement(abundant_nums, 2) if x+y < 28124])
print sum(a.difference(b))