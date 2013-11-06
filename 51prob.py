from eulertools import primes
from itertools import combinations
from operator import add

def idx_of_repeats(num):
    ''' Returns indices of repeating numbers '''
    num = map(int, str(num))
    idx_list = []
    for n in set(num):
        if num.count(n) == 2:
            idx_list.append( [idx for idx, j in enumerate(num) if j == n] )
    return idx_list
    
prime_list = filter( lambda x: len(str(x)) == 7 and len(set(str(x))) != len(str(x)), primes(10**6))
prime_set = set(prime_list)
prime_dict = {}

