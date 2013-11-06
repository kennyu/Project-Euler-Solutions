from eulertools import primes

prime_list = primes(100000)
prime_set  = set(prime_list)
prime_sum = 0
counter = 0

def is_truncable(prime):
    prime = str(prime)
    for x in xrange(1, len(str(prime))):
        if not int(prime[-x:]) in prime_set:
            return False
        if not int(prime[:x]) in prime_set:
            return False
    return True

for p in prime_list[4:]:
    if is_truncable(p):
        print p
        prime_sum += p
        counter += 1
    if counter == 11:
        break
print prime_sum