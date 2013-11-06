from itertools import permutations

mult_set = set()
for p in permutations('123456789'):
    if int(p[0]+p[1]) * int(p[2]+p[3]+p[4]) == int(p[5]+p[6]+p[7]+p[8]):
        mult_set.add(int(p[5]+p[6]+p[7]+p[8]))
    if int(p[0]) * int(p[1]+p[2]+p[3]+p[4]) == int(p[5]+p[6]+p[7]+p[8]):
        mult_set.add(int(p[5]+p[6]+p[7]+p[8]))
print sum(mult_set)