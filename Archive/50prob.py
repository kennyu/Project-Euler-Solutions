from eulertools import primes

primes_list = filter( lambda x : x < 1000000 , map(int, primes(79000)))
primes_set = set(primes_list)

max_len = 0
prime_sum = 0

for idx in xrange(len(primes_list)):
    for idx2 in xrange(idx+1, len(primes_list)):
        sum_of_primes = sum( primes_list[idx:idx2+1])
        if sum_of_primes >= 1000000:
            break
        if sum_of_primes in primes_set:
            if idx2 - idx > max_len:
                max_len = idx2 - idx
                prime_sum = sum_of_primes
