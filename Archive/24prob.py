from itertools import permutations
total_list = list(permutations('0123456789'))
total_list.sort()
print reduce(lambda x,y: x+y, total_list[999999], '')