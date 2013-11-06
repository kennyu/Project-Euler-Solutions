primes = [True]*1999999

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
print sum(primes_list)