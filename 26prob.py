# from decimal import *

# getcontext().prec = 2000

# def cycle(x):
    # ''' Returns cycle length '''
    # if len(str(x)[2:]) < getcontext().prec-5:
        # return 0
    # elif is_repeating(str(x)[2:getcontext().prec-5]):
        # return 1
    # else:
        # return cycle_len(str(x)[2:getcontext().prec-5])
    
# def is_repeating(n):
    # ''' checks if the last 20 numbers are repeats '''
    # return len(set(n[-20:])) == 1
    
# def cycle_len(x):
    # ''' Quick and dirty way to find repeating consecutive substrings '''
    # x = list(x)[::-1]
    # for snd_idx in range(2, len(x)):
        # current_dist = snd_idx
        # if x[0] == x[snd_idx] and x[0:current_dist] == x[ snd_idx : snd_idx+current_dist]:
            # return current_dist
 
# max_cycle = 0
# d = 0
# for x in xrange(2, 1000):
    # cycle_of_x = cycle( Decimal(1) / Decimal(x))
    # if cycle_of_x > max_cycle:
        # max_cycle = cycle_of_x
        # d = x

# print d

# Project Euler Forums
import itertools
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    for i in itertools.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)

len,i = max((recur_len(i),i) for i in range(2,1000))
print i