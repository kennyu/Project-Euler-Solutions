from eulertools import primes

circular_primes = set()
prime_set  = set(primes(100000))

def is_circular(prime):
    for x in xrange(1,len(str(prime))):
        if not int(rotate(str(prime), x)) in prime_set:
            return False
    return True
    
def rotate(strg,n):
''' Rotates a string to the left by n characters '''
    return strg[n:] + strg[:n]

for p in filter( lambda x: x < 10**6 , prime_set):
    if is_circular(p):
        circular_primes.add(p)
        
print len(circular_primes)
