from eulertools import primes
from itertools import count

prime_set = set(primes(10000))

def test(a , b):
    formula = lambda x: (x**2) + (a*x) + b
    prime_count = 0
    for num in count(0):
        if formula(num) in prime_set:
            prime_count += 1
        else:
            break
    return prime_count
    
max_prime_count = 0
current_coeff = 0 , 0

for a in xrange(-999, 1000):
   for b in xrange(-999, 1000):
       consec_primes = test(a,b)
       if consec_primes > max_prime_count:
           max_prime_count = consec_primes
           current_coeff = a, b
           print current_coeff
            
print current_coeff[0] * current_coeff[1]
# -59231
