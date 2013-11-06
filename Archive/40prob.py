from itertools import count

nums = [10**x for x in xrange(6, -1,-1)]
frac_part = []
next_num = nums.pop()
n = 0
for x in count(1):
    if n <= next_num and next_num <= len(str(x)) + n:
        frac_part.append(int(str(x)[next_num-n-1]))
        print frac_part
        if not nums: break
        next_num = nums.pop()
    n += len(str(x))
    
print reduce(lambda x,y: x*y , frac_part, 1 )