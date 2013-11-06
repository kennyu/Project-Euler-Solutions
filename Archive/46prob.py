from eulertools import primes

prime_set = set(map(int, primes(5000)))
sq_list = map(lambda x: 2*(x**2), range(1,100))
       
def is_goldbach_num(x):
    for s in sq_list:
        if x - s in prime_set:
            return True
        if s > x:
            return False
    return False
    
for x in xrange(9,10000):
    if x not in prime_set and x % 2 == 1:
        if not is_goldbach_num(x):
            print x
            break
            