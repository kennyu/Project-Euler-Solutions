from eulertools import primes
from itertools import permutations

p = set(primes(10000000))

# def is_pandigital(p):   
    # num_list = map(int, list(str(p)))
    # num_list.sort()
    # n = len(num_list)
    # while num_list:
        # if n == num_list.pop():
            # n -= 1
        # else:
            # return False
        # if not num_list:
            # return True
    # return False

# for x in reversed(p):
    # if is_pandigital(x):
        # print x
        # break

# Another solution from euler forums
def tup_to_int(n):
    return int(reduce( lambda x, y : x+y , i ,'' ))
    
print max( [ tup_to_int(i) for i in permutations('1234567') if tup_to_int(i) in p ] )

# 7652413