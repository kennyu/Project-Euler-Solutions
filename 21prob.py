from eulertools import prime_factors , primes
from itertools import product
from operator import mul

prime_list = primes(1500)
def sum_proper_divisors(num):
''' Returns the sum of the proper divisors '''
    factors = list(prime_factors(num,prime_list))
    total = 0
    primes = map(lambda x: x[0] , factors)
    expons = map(lambda x: x[1] , factors)
    for expon_list in  product( *map(lambda x: range(x+1), expons) ):
        if list(expon_list) != expons:
            total += reduce( mul ,map( lambda x, y : x**y , primes, expon_list), 1)
    return total

amicable_list = []
for x in xrange(2,10000):
    a = sum_proper_divisors(x)
    b = sum_proper_divisors(a)
    if b == x and not b == a:
        amicable_list.append(x)

print sum(amicable_list)

    