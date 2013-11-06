def prime_factors(num, primes_list=None):
    if primes_list == None:
        primes_list = map(int, primes(10**5))
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
        
def primes(n):
    file_name = 'primes.txt' if n > 10**5 else 'primes_small.txt'
    with open('primes.txt', 'r') as file:
        prime_list = file.read().strip().split()[:n]
        return map(int, prime_list)
    
#Generate 100mm primes and write to primes.txt
#Generate 100,000 primes and write to primes_small.txt
# if __name__ == '__main__':
    # primes_list = []
    # primes = [True]*(10**5 + 2)
    # for idx, a in enumerate(primes):
        # if idx == 0 or idx == 1:
            # primes[idx] = False
            # continue
        # if a == True:
            # primes_list.append(idx)
            # start = idx*2
            # while start < len(primes):
                # primes[start] = False
                # start += idx
    # del(primes)
    # file = open('primes_small.txt', 'w')
    # file.writelines(map(lambda x: str(x) + ' ', primes_list))
    # file.close()