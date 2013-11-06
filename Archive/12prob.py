def next_triag():
    triag[1] += 1
    triag[0] += triag[1]
     
def factor_generator(num):
    factor_list = []
    while True: 
        for p in primes_list:
            if num % p == 0:
                factor_list.append(p)
                num /= p
                break
        if num == 1:
            break
    factor_set = set(factor_list)
    for elem in factor_set:
        yield (elem, factor_list.count(elem))

def number_of_divisors(num):
    divisors = 1
    for prime , multip in factor_generator(num):
        multip += 1
        divisors *= multip
    return divisors
    
primes_list = []
primes = [True]*100000
for idx, a in enumerate(primes):
    if idx == 0 or idx == 1:
        primes[idx] = False
        continue
    if a == True:
        primes_list.append(idx)
        start = idx*2
        while start < len(primes):
            primes[start] = False
            start += idx
del(primes)

triag = [1,1]
for a in xrange(100000):
    divisors = number_of_divisors(triag[0]) 
    if divisors > 500:
        print triag[0]
        break
    else:
        next_triag()
