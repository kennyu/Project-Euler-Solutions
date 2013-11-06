# import primes

# prime_list = open('primes.txt', 'r').read().strip().split()[:1000000]
# prime_list = map(int, prime_list)

# x = []
# n = 4
# while True:

    # if len(list(primes.factor_generator(n, prime_list))) == 4:
        # x.append(n)
    
    # if len(x[-4:]) == 4 and x[-4] == x[-3]-1 == x[-2]-2 == x[-1]-3:
        # print x[-4]
        # break
        
    # n += 1

# COMBINATION OF SIEVE AND CHECKING
        
limit=1000000     # Search under 1 million for now
factors=[0]*limit # number of prime factors.
count=0
for i in xrange(2,limit):
    if factors[i]==0:
        # i is prime
        count =0
        val =i
        while val < limit:
            factors[val] += 1
            val+=i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print i-3 # First number
            break
    else:
        count = 0