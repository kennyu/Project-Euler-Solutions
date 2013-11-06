primes = [True]*10000


for idx, a in enumerate(primes):
    if idx == 0 or idx == 1:
        primes[idx] = False
        continue
    if a == True:
        start = idx*2
        while start < len(primes):
            primes[start] = False
            start += idx
            
            
primes_list = []
for idx, a in enumerate(primes):
    if a:
        primes_list.append(idx)
    

prime_factors = []    
num = 600851475143 
while not num == 1:
    for p in primes_list:
        if num % p == 0:
            prime_factors.append(p)
            num /= p
            break

print max(prime_factors)